from main import execute

execute([
    0x10, 0x00,  # lda 0x00 ; reset A
    0x11, 0x01,  # ldb 0x01 ; set B to 1
    0xe0,        # prn      ; print A
    0x20,        # add      ; add A and B
    0x11, 0xff,  # ldb 0xff ; set it to this so we can see if eaq
    0x24,        # eaq      ; is A and B equal
    0xe3, 0x01,  # jnz 0x01 ; jump back to print
    0xe0,        # prn      ; print again (last character we missed)
    0xfd,        # deb      ; Dump memory to terminal
    0x21,        # sub      ; Subtract 1
    0xeb,        # wmem     ; Write to memory
    0xfd,        # deb      ; Dump memory to terminal
    0x10, 0x00,  # lda 0x00 ; reset A
    0x11, 0x00,  # ldb 0x00 ; and B
    0xec,        # rmem     ; read from memory
    0xe0,        # prn      ; print what we got
    0xff         # hlt      ; Halt
], addon="None")