"""
jris5252 assembler
- Written by jasedxyz <jased@jased.xyz>
"""

import sys

args = sys.argv

print("""jris5252 assembler v1
===========""")

file = ""
outfile = ""

with open(args[1], "r") as f:
  file = f.read()


outfile = """from main import execute
execute([
Code Go Here
])""".replace("Code Go Here", file)

outfile = outfile.replace("lda", "0x10,")
outfile = outfile.replace("ldb", "0x11,")
outfile = outfile.replace("ldc", "0x12,")
outfile = outfile.replace("sab", "0x13,")
outfile = outfile.replace("sbc", "0x14,")
outfile = outfile.replace("sac", "0x15,")

outfile = outfile.replace("add", "0x20,")
outfile = outfile.replace("sub", "0x21,")
outfile = outfile.replace("mul", "0x22,")
outfile = outfile.replace("grt", "0x23,")
outfile = outfile.replace("eaq", "0x24,")

outfile = outfile.replace("prn", "0xe0,")
outfile = outfile.replace("get", "0xe1,")

outfile = outfile.replace("jmp", "0xe2,")
outfile = outfile.replace("jnz", "0xe3,")
outfile = outfile.replace("jta", "0xe4,")
outfile = outfile.replace("jtb", "0xe5,")

outfile = outfile.replace("wmem", "0xeb,")
outfile = outfile.replace("rmem", "0xec,")

outfile = outfile.replace("nop", "0xea,")
outfile = outfile.replace("deb", "0xfd,")
outfile = outfile.replace("hlt", "0xff")

with open("out.jris.py", "w") as f:
  f.write(outfile)