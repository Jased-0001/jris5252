def preload(memory:list):
  return ({
    "author": "jasedxyz",
    "name": "Breakpoints",
    "version": "v1"
  }, memory)

def onCycle(memory:list,registers:dict):
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  if registers["ins"] == 0xbb:
    print("BREAKPOINT:")
    print(registers)
    print(memory)
    input("Hit enter to continue execution")
    return (True, memory, registers)
  return (False, memory, registers)

def stop(memory:list,registers:dict):
  return (memory, registers, False)