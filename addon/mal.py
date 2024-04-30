import os, types



malPlugins = os.listdir(os.getcwd() + "/addon/malPlugins")
malNamespace = types.SimpleNamespace()
def preload(memory:list):
  for i in malPlugins:
    if i.split(".")[len(i.split(".")) - 1] == "py":
      exec(f"""import os
from addon.malPlugins import {i.replace(".py", "")}
_malTemp = {i.replace(".py", "")}.preload({memory})
    """, malNamespace.__dict__)
      verString = malNamespace._malTemp[0]
      memory = malNamespace._malTemp[1]
      print(f"Loaded malPlugin {verString}")
    
  
  return ({
    "author": "jasedxyz",
    "name": "Multi Plugin Loader",
    "version": "1"
  }, memory)

def onCycle(memory:list,registers:dict):
  for i in malPlugins:
    if i.split(".")[len(i.split(".")) - 1] == "py":
      exec(f"""
_malTemp = {i.replace(".py", "")}.onCycle({memory}, {registers})
    """, malNamespace.__dict__)
      memory = malNamespace._malTemp[0]
      registers = malNamespace._malTemp[1]
      
  return (memory, registers)

def insNotFound(memory:list,registers:dict):
  for i in malPlugins:
    if i.split(".")[len(i.split(".")) - 1] == "py":
      exec(f"""
_malTemp = {i.replace(".py", "")}.insNotFound({memory}, {registers})
    """, malNamespace.__dict__)
      found = malNamespace._malTemp[0]
      memory = malNamespace._malTemp[1]
      registers = malNamespace._malTemp[2]
      if found:
        return (True, memory, registers)
      
  return (False, memory, registers)

def stop(memory:list,registers:dict):
  for i in malPlugins:
    if i.split(".")[len(i.split(".")) - 1] == "py":
      exec(f"""
  _malTemp = {i.replace(".py", "")}.stop({memory}, {registers})
    """, malNamespace.__dict__)
      memory = malNamespace._malTemp[0]
      registers = malNamespace._malTemp[1]
      wannaStop = malNamespace._malTemp[2]
      if wannaStop:
        return (memory, registers, True)
  return (memory, registers, False)