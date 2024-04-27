from . import random as rand

import random

from main import execute


def preload(memory:list):
  randverstring, memory = rand.preload(memory)
  print("Cryptography imported random addon: ", randverstring)
  
  return ({
    "author": "jasedxyz",
    "name": "cryptography",
    "version": "v2"
  }, memory)

def onCycle(memory:list,registers:dict):
  memory, registers = rand.onCycle(memory, registers)
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  didRandHandleIt, memory, registers = rand.insNotFound(memory, registers)
  if didRandHandleIt:
    return (True, memory, registers)
    
  elif registers["ins"] == 0x27: # keyg
    if registers["mci"] == 0xff:
      for i in range(0,4):
        memory[registers["mcd"] + i] = random.randint(0x00, registers["maxSize"])
      registers["mci"] = 0x00
      registers["mcd"] = 0x0
    elif registers["mci"] != 0xff:
      registers["mci"] = registers["ins"]
    return (True, memory, registers)

  elif registers["ins"] == 0x28: # bsftr
    registers["a"] = registers["a"] >> registers["b"]
    return (True, memory, registers)

  elif registers["ins"] == 0x29: # bsftl
    registers["a"] = registers["a"] << registers["b"]
    return (True, memory, registers)

  else:
    return (False, memory, registers)

def stop(memory:list,registers:dict):
  memory, registers, doesRandWannaStop = rand.stop(memory, registers)
  return (memory, registers, doesRandWannaStop)