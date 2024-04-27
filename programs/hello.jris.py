from main import execute

execute([
  0x10, ord("H"), # lda "H"  ; data to print
  0x11, 0xf9,     # ldb 0xf9 ; address to write to
  0xeb,           # wmem     ; write it to memory
  0xe0,           # prn      ; print the character
  
  0x10, ord("e"), # lda "e"  ; data to print
  0x11, 0xfa,     # ldb 0xfa ; address to write to
  0xeb,           # wmem     ; write it to memory
  0xe0,           # prn      ; print the character
  
  0x10, ord("l"), # lda "l"  ; data to print
  0x11, 0xfb,     # ldb 0xfb ; address to write to
  0xeb,           # wmem     ; write it to memory
  0xe0,           # prn      ; print the character
  
  0x11, 0xfc,     # ldb 0xfc ; address to write to
  0xeb,           # wmem     ; write it to memory
  0xe0,           # prn      ; print the character
  
  0x10, ord("o"), # lda "o"  ; data to print
  0x11, 0xfd,     # ldb 0xfd ; address to write to
  0xeb,           # wmem     ; write it to memory
  0xe0,           # prn      ; print the character

  0xff            # hlt
])