import random


def preload(memory:list):
  for i in range(len(memory)):
    memory[i] = random.randint(0x00, 0xfe)
    if memory[i] == 0xe2 or memory[i] == 0xe3 or\
      memory[i] == 0xe4 or memory[i] == 0xe:
      memory[i] = 0xea
  
  print(memory)
    
  return ({
    "author": "jasedxyz",
    "name": "Rom Randomizer",
    "version": "v1"
  }, memory)

def onCycle(memory:list,registers:dict):
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  return (False, memory, registers)

def stop(memory:list,registers:dict):
  return (memory, registers, False)