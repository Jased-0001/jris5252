from main import execute

execute([
  0x25,       # rand
  0x15,       # sac
  0xe0,       # prn
  0x27, 0x30, # keyg 0x30 ; Generate 4 byte random key at 0x30
  0x11, 0x30, # ldb 0x30
  0xec,       # rmem
  0xe0,       # prn
  0x10, 0x01, # lda 0x01
  0x20,       # add
  0x13,       # sab
  0x10, 0x34, # lda 0x34 ; end addr
  0x24,       # eaq
  0xe3, 0x06, # jnz 0x06
  0x10, "\n", # lda "\n"
  0xe0,       # prn
  0x11, 0x30, # ldb 0x30
  0xec,       # rmem
  0xe0,       # prn
  0x11, 0x31, # ldb 0x31
  0x28,       # bsftr
  0xe0,       # prn
  0x29,       # bsftl
  0xe0,       # prn
  0xff        # hlt
], addon="cryptography")