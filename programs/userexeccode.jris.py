execute([
  0xe1,       # get      ; Get character
  0xe0,       # prn      ; and print it      
  0x13,       # sab      ; Switch A and B
  0xe1,       # get      ; Get character
  0xe0,       # prn      ; and print it
  0xeb,       # wmem     ; Write
  0xe4,       # jta      ; Jump to address
  0xff        # hlt      ; Halt
])