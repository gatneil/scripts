import subprocess
from Find import *

files = FindFiles()
for f in files:
    command = ['sed', '--in-place', 's/[[:space:]]\+$//', f]
    subprocess.check_output(command)
