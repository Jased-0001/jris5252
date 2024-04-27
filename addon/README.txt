There are three required functions for an addon:

preload - Runs before the CPU starts execution
Gets passed in memory (list)
Expected to return memory (list) and information
        - about the addon (dict)
        - Example:
        - {
        -   "author": "jasedxyz <https://jased.xyz/>",
        -   "name: "random",
        -   "version": "v1"
        - }

onCycle - Runs before the switch ladder in the
        - CPU.
Gets passed in memory (list) and registers (dict)
Expected to return memory (list) and registers (dict)
        - in a tuple (memory, registers)

insNotFound - Use to create custom instructions.
            - Access to registers, use "ins" in
            - the dict.
Gets passed in memory (list) and registers (dict)
Expected to return if the instruction was found
            - and was executed successfully.
            - Use true to indicate it was found
            - Return also
            - memory (list) and registers (dict)
            - in a tuple 
            - (bool, memory, registers)

stop - CPU is halting, run some final code.
Gets passed in memory (list) and registers (dict)
Expected to return memory, registers, and wether or
     - not the addon wants to keep executing,
     - all in a tuple.