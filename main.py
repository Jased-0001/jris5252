import types
from time import sleep

from getkey import getkey


# Custom exceptions
class RegisterOverflow(Exception):

  def __init__(self, message, register):
    super().__init__(message)
    self.register = register


class MemoryOverflow(Exception):

  def __init__(self, message, shrinkToMaximum):
    super().__init__(message)
    self.sTM = shrinkToMaximum


class NoRomFound(Exception):
  pass


def dump(memory: list = [],
         registers: dict = {},
         dumpRegisters: bool = True,
         dumpMemory: bool = True,
         dumpDecryptedMemory: bool = True):
  if len(memory) == 0:
    dumpMemory = False
    dumpDecryptedMemory = False
  if dumpRegisters:
    print(registers)
  if dumpMemory:
    print(memory)
  if dumpDecryptedMemory:
    for i in memory:
      print(chr(i), end="", flush=True)


def replaceStringsWithDecimalValue(memory: list):
  # last thing before execution:
  # Replace strings with decimal value
  # This works apparently?????????

  # Used to know if we found every string
  notfoundall = True
  found = 0

  # While we haven't found every string...
  while notfoundall:
    # reset the values
    notfoundall = False
    found = 0

    # and loop through the memory
    for i in range(len(memory)):
      # Is it longer than one byte and is it not an integer?
      if not isinstance(memory[i], int) and len(memory[i]) != 1:
        _TEMP = []

        # Loop through every byte in the string and append
        # the ord value to _TEMP
        for x in memory[i]:
          _TEMP.append(ord(x))

        # Put it where we found the string
        memory[i] = _TEMP

        # "Unpack" the list we made (I DONT KNOW HOW THIS WORKS)
        memory = memory[:i] + memory[i] + memory[i + 1:]
        found += 1
    notfoundall = found != 0

  for i in range(len(memory)):
    if not isinstance(memory[i], int):
      memory[i] = ord(memory[i])

  return memory


def execute(rom: list = [],
            ram: list = [],
            ram_size: int = -1,
            ignore_overflow: bool = False,
            speed: int = 0,
            noinfo: bool = False,
            maxSize: int = 0xff,
            endDebDisable: bool = False,
            addon: str = "None") -> tuple:
  # Get memory stuff

  # No rom
  if len(rom) == 0:
    raise NoRomFound("No rom!")

  rom = replaceStringsWithDecimalValue(rom)

  # stuff to create blank ram if not already exists
  # will ignore ram_size if ram already there
  if len(ram) > 0:
    ram = replaceStringsWithDecimalValue(ram)
    ram_size = len(ram)
  else:
    if ram_size == -1:
      ram_size = maxSize - len(rom)
    if ram_size != 0:
      for _ in range(ram_size):
        ram.append(0x00)

  memory = []

  # put rom and ram into the same memory map
  for i in rom:
    memory.append(i)
  for i in ram:
    memory.append(i)

  addonNamespace = types.SimpleNamespace()

  if addon != "None":
    exec(f"from addon import {addon}", addonNamespace.__dict__)
    exec(f"_preload = {addon}.preload(memory={memory})",
         addonNamespace.__dict__)
    addonInfo = addonNamespace._preload[0]
    memory = addonNamespace._preload[1]
    print(
        f"Loaded addon {addonInfo['name']} version {addonInfo['version']} ({addon}) \
by {addonInfo['author']}")

  if not noinfo:
    print(f"""System Information:
    Ram size = {len(ram)} Bytes
    Rom size = {len(rom)} Bytes
    Memory   = {len(memory)} Bytes
    Maximum  = {maxSize} bytes
    {'We will ignore overflows' if ignore_overflow else 'Do not ignore overflows.'}
    {f'Speed is is {1/speed} Hz' if speed>0 else ''}""")

  # Define the 3 user registers, program register
  # the MultiCycle registers and the current instruction
  registers = {
      "a": 0x00,
      "b": 0x00,
      "c": 0x00,
      "prg": 0x00,
      "mci": 0x00,  #MultiCycleInstruction
      "mcd": 0x00,  #MultiCycleData temp
      "ins": 0x00,
      # Registers for addons
      "maxSize": maxSize,
      "noinfo": noinfo,
  }

  # make sure program register is at zero
  registers["prg"] = 0x00

  # run!
  running = True

  while running:
    try:
      # print(f"  Program Register = {registers['prg']} read {memory[registers['prg']]}")

      registers["ins"] = memory[registers["prg"]]

      if addon != "None":
        exec(
            f"_TEMPADDON={addon}.onCycle(memory={memory},registers={registers})",
            addonNamespace.__dict__)
        memory = addonNamespace._TEMPADDON[0]
        registers = addonNamespace._TEMPADDON[1]

      # Multi cycle instruction
      # if it was set to an instruction we move
      # the registers around to get the data where
      # we want
      if registers["mci"] != 0x00:
        registers["mcd"] = memory[registers["prg"]]
        registers["ins"] = registers["mci"]
        registers["mci"] = 0xff

      match registers["ins"]:
      # Registers

        case 0x10:  # LDA
          if registers["mci"] == 0xff:  # success
            registers["a"] = registers["mcd"]
            registers["mci"] = 0x00
            registers["mcd"] = 0x00
          elif registers["mci"] != 0xff:
            registers["mci"] = registers["ins"]

        case 0x11:  # LDB
          if registers["mci"] == 0xff:  # success
            registers["b"] = registers["mcd"]
            registers["mci"] = 0x00
            registers["mcd"] = 0x00
          elif registers["mci"] != 0xff:
            registers["mci"] = registers["ins"]

        case 0x12:  # LDC
          if registers["mci"] == 0xff:  # success
            registers["c"] = registers["mcd"]
            registers["mci"] = 0x00
            registers["mcd"] = 0x00
          elif registers["mci"] != 0xff:
            registers["mci"] = registers["ins"]

        case 0x13:  # SAB
          registers["mcd"] = registers["b"]
          registers["b"] = registers["a"]
          registers["a"] = registers["mcd"]
          registers["mcd"] = 0x00

        case 0x14:  # SBC
          registers["mcd"] = registers["c"]
          registers["c"] = registers["b"]
          registers["b"] = registers["mcd"]
          registers["mcd"] = 0x00

        case 0x15:  # SAC
          registers["mcd"] = registers["c"]
          registers["c"] = registers["a"]
          registers["a"] = registers["mcd"]
          registers["mcd"] = 0x00

        # Math

        case 0x20:  # ADD
          registers["a"] += registers["b"]
        case 0x21:  # SUB
          registers["a"] -= registers["b"]
        case 0x22:  # MUL
          registers["a"] *= registers["b"]
        case 0x23:  # GRT
          registers["c"] = 0x00 if registers["a"] > registers["b"] else 0x01
        case 0x24:  # EAQ
          registers["c"] = 0x00 if registers["a"] == registers["b"] else 0x01

        # Other/Misc

        case 0xe0:  # PRN
          print(chr(registers["a"]), end="", flush=True)
        case 0xe1:  # GET
          registers["a"] = ord(getkey())  # Ignore any error here, it works
        case 0xe2:  # JMP
          if registers["mci"] == 0xff:  # success
            registers["prg"] = registers["mcd"]
            registers["mci"] = 0x00
            registers["mcd"] = 0x0
          elif registers["mci"] != 0xff:
            registers["mci"] = registers["ins"]

        case 0xe3:  # JNZ
          # We still want to make this multi-cycle so we dont get an exception
          if registers["mci"] == 0xff:  # success
            if registers["c"] != 0x00:
              registers["prg"] = registers["mcd"]
            registers["mci"] = 0x00
            registers["mcd"] = 0x0
          elif registers["mci"] != 0xff:
            registers["mci"] = registers["ins"]

        case 0xe4:  # JTA
          registers["prg"] = registers["a"]

        case 0xe5:  # JTB
          registers["prg"] = registers["b"]

        case 0xea:  # NOP
          pass

        case 0xeb:  # WMEM
          memory[registers["b"]] = registers["a"]

        case 0xec:  # RMEM
          registers["a"] = memory[registers["b"]]

        case 0xfd:  # DEB
          dump(memory, registers)

        case 0xff:  # HLT
          running = False

        case _:
          if addon != "None":
            exec(
                f"_canRun = {addon}.insNotFound(memory={memory}, registers={registers})",
                addonNamespace.__dict__)
            memory = addonNamespace._canRun[1]
            registers = addonNamespace._canRun[2]

            if addonNamespace._canRun[0]:
              pass
            else:
              print(
                  f"  [!] CPU exception (instruction {memory[registers['prg']]} is unknown)"
              )
              pass
          else:
            print(
                f"  [!] CPU exception (instruction {memory[registers['prg']]} is unknown)"
            )
            pass

      if running:
        if speed > 0:
          sleep(1 / speed)

        registers["prg"] += 0x01

        if registers["prg"] >= len(memory):
          running = False

        if not ignore_overflow:
          if registers["a"] > maxSize:
            raise RegisterOverflow("Register Overflow", "a")
          if registers["b"] > maxSize:
            raise RegisterOverflow("Register Overflow", "b")
          if registers["c"] > maxSize:
            raise RegisterOverflow("Register Overflow", "c")

          if len(memory) > maxSize:
            raise MemoryOverflow\
              (f"Memory size is too large! ({len(memory)} > maximum {maxSize})", True)
      else:
        if addon != "None":
          exec(
              f"_stoppingData = {addon}.stop(memory={memory}, registers={registers})",
              addonNamespace.__dict__)
          memory = addonNamespace._stoppingData[0]
          registers = addonNamespace._stoppingData[1]
          running = addonNamespace._stoppingData[2]
        if not endDebDisable and not running:
          dump(memory, registers)
          return (memory, registers)

    except MemoryOverflow as e:
      print(f"  [!] CPU exception ({e}, trimming)")
      if e.sTM:
        while len(memory) != maxSize:
          memory.pop()
      else:
        for _ in range(len(memory) - (len(rom) + ram_size)):
          memory.pop()
    except RegisterOverflow as e:
      print(f"  [!] Register Overflow! (resetting {e.register})")
      exec(f"registers[\"{e.register}\"] = 0x00")
    except Exception as e:
      print(f"  [!] CPU exception ({e}, dumping)")
      running = False
      dump(memory, registers)


def demo():
  execute([
      0x11,
      0x10,
      0xec,
      0xe0,
      0x10,
      0x1D,
      0x24,
      0x13,
      0x11,
      0x01,
      0x20,
      0x13,
      0xe3,
      0x01,
      0xff,
      0xea,
      "Hello, world!",
      0x00,
  ],
          endDebDisable=False)


if __name__ == "__main__":
  try:
    with open("out.jris.py", "r") as f:
      exec(f.read())
  except FileNotFoundError:
    demo()
