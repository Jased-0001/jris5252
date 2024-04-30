from main import execute

execute([
  0x11, 0x0f, # ldb 0x0f ; mem address to start at
  0xe1,       # get      ; Get character
  0xe0,       # prn      ; Print
  0x13,       # sab
  0x11, 0x01, # ldb 0x01
  0x20,       # add
  0xeb,       # wmem
  0x13,       # sab
  0xe2, 0x02, # jmp 0x02 ; Jump
  0xfd,       # deb      ; debug
  0xff        # hlt      ; Halt
])