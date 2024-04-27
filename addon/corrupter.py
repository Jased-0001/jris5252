import random

def preload(memory:list):
  return ({
    "author": "jasedxyz",
    "name": "Corrupter",
    "version": "v1"
  }, memory)

def onCycle(memory:list,registers:dict):
  memory[random.randint(0x00,0xff)] = random.randint(0x00,0xff)
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  return (False, memory, registers)

def stop(memory:list,registers:dict):
  return (memory, registers, False)