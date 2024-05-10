# jris5252
Jasedxyz's Reduced Instruction Set 5252 CPU... thing

## How to use
Use Python Poetry ``poetry install`` to install the
dependencies, then import the ``main.py`` file.

Example:
```python
from main import execute

execute([
  0xff # hlt
])
```

The instruction set is located in the root of the project in the
``jris.txt`` file.

## Addons
Addons are a way to add new instructions or functionality. 
To use them in a project, add the addons argument with a string.

```python
from main import execute

execute([
  
], addon="addonNameHere")
```

This will load an addon from the ``addon/`` folder.

To make your own, duplicate the ``example.py`` file view the ``README.txt``
file located in the addon folder.

Using addons, you can:
- manipulate the memory
- manipulate the registers
- add extra registers
- add more instructions

## Registers
### User Registers
- ``a`` register
- ``b`` register
- ``c`` register
### Internal Registers
- ``prg`` Program register
- ``mci`` MultiCycleInstruction
- ``mcd`` MultiCycleData
- ``ins`` Instruction - contains current instruction
### Misc Registers (use with addons)
- ``maxSize`` Max size before overflow
- ``noinfo`` Display no info from the cpu

## ``execute()`` arguments (in order)
- rom - list
  - Required. Contains instructions to run
- ram - list
  - Optional. Contains ram defined from program to load into CPU
- ram_size - int
  - Optional, defaults to the maximum. Use to choose how much RAM you want in bytes
- ignore_overflow - bool
  - Optional, defaults to false. Use to ignore register and memory overflows
- noinfo - bool
  - Optional, defaults to false. Use if you don't want the CPU to output its information
    - Information is how much memory the CPU can access
- maxSize - int
  - Optional, defaults to 0xff (255). Use to change the maximum register and memory size
- endDebDisable - bool
  - Optional, defaults to false. Basically just dumps the memory upon the CPU halting
- addon - str
  - Optional. Use for addons

