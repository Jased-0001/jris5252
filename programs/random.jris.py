from main import execute

execute(rom=[
  0x25,       # rand        ; Get a random number
  0x15,       # sac         ; Switch A and C (move random number)
  0xe0,       # prn         ; Print it
  0x11, 0xb0, # ldb 0xb0    ; Load B with 0xb0 to write it to memory
  0xeb,       # wmem        ; Write it to memory
  
  0x25,       # rand        ; Get a random number
  0x15,       # sac         ; Switch A and C (move random number)
  0xe0,       # prn         ; Print it
  0x11, 0xb1, # ldb 0xb1    ; Load B with 0xb1 to write it to memory
  0xeb,       # wmem        ; Write it to memory
  
  0x26, 0x0f, # randwm 0x0f ; Get a random number with a max of 0x0f
  0x15,       # sac         ; Switch A and C (move random number)
  0xe0,       # prn         ; Print it
  0x11, 0xb2, # ldb 0xb2    ; Load B with 0xb2 to write it to memory
  0xeb,       # wmem        ; Write it to memory
  
  0xff        # hlt
], addon="random", maxSize=0xff, endDebDisable=False)