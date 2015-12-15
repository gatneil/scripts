import json
from os import listdir
from os.path import isfile, join
from Common import *

def FindFiles():
    res = []
    for folder in folders:
        fp = bp + folder + '/'
        af = [f for f in listdir(fp) if isfile(join(fp, f))]
        jf = [f for f in af if 'json' in f and 'parameters' not in f and 'metadata' not in f and 'UiDefinition' not in f]
        for f in jf:
            res.append(fp + f)

    return res
        

