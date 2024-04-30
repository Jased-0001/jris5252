from main import execute

execute([       # ; Ignore all the debs, testing
  0x10, 0xffff, # lda 0xffff
  0xfd,         # deb
  0x15,         # sac
  0xfd,         # deb
  0x14,         # sbc
  0xfd,         # deb
  0x13,         # sab
  0xfd,         # deb
  0x11, 0x0001, # ldb 0x0001 
  0xfd,         # deb
  0x20,         # add
  0xfd,         # deb
  0xff          # hlt
], maxSize=0xffff, endDebDisable=True, ram_size=0)