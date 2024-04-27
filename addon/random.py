import random


def preload(memory:list):
  return ({
    "author": "jasedxyz <https://jased.xyz/>",
    "name": "random",
    "version": "v1"
  }, memory)

def onCycle(memory:list,registers:dict):
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  if registers["ins"] == 0x25: # rand
    registers["c"]  = random.randint(0x00, registers["maxSize"])
    return (True, memory, registers)
  elif registers["ins"] == 0x26:
    if registers["mci"] == 0xff: # randwm
      registers["c"] = random.randint(0x00, registers["mcd"])
      registers["mci"] = 0x00
      registers["mcd"] = 0x0
    elif registers["mci"] != 0xff:
      registers["mci"] = registers["ins"]
    return (True, memory, registers)
  else:
    return (False, memory, registers)

def stop(memory:list,registers:dict):
  return (memory, registers, False)