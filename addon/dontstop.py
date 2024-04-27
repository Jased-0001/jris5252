def preload(memory:list):
  return ({
    "author": "jasedxyz",
    "name": "Don't Stop",
    "version": "v1"
  }, memory)

def onCycle(memory:list,registers:dict):
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  return (False, memory, registers)

def stop(memory:list,registers:dict):
  registers["prg"] += 1
  return (memory, registers, True)