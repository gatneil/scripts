from GenSingle import *
from Find import *

files = FindFiles()
for f in files:
    GenSingle(f)
