import json
#import simplejson as json
import collections
import os.path
from Common import *

params = {}
for folder in folders:
    path = bp + folder + '/azuredeploy.parameters.json'
    if not os.path.isfile(path):
        print("skipped: " + path)

    else:
        print("parsing: " + path)
        with open(path, 'r') as pf:
            j = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(pf.read())

        for param in j['parameters']:
            if param not in params:
                params[param] = True

for param in params:
    print(param)
    

    
