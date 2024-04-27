def preload(memory:list):
  return ({
    "author": "",
    "name": "",
    "version": ""
  }, memory)

def onCycle(memory:list,registers:dict):
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  return (False, memory, registers)

def stop(memory:list,registers:dict):
  return (memory, registers, False)