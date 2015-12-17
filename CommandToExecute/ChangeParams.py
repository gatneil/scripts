import simplejson as json
import collections
import os.path
from Common import *

replacements = {'storageAccountPrefix': 'GEN-UNIQUE-8', 'replicatorPassword': 'GEN-PASSWORD', 'newStorageAccountName': 'GEN-UNIQUE-8', 'storageNameForFrontEnd': 'GEN-UNIQUE-8', 'mySqlPassword': 'GEN-PASSWORD', 'administratorLoginPassword': 'GEN-PASSWORD', 'dnsName': 'GEN-UNIQUE-8', 'datastaxPassword': 'GEN-PASSWORD', 'opsCenterAdminPassword': 'GEN-PASSWORD', 'storageAccountNamePrefix': 'GEN-UNIQUE-8', 'adminPassword': 'GEN-PASSWORD', 'clusterName': 'GEN-UNIQUE-8', 'replicaSetKey': 'GEN-SSH-PUB-KEY', 'domainName': 'GEN-UNIQUE-8', 'dnsNameForPublicIP': 'GEN-UNIQUE-8', 'storageAccountName': 'GEN-UNIQUE-8', 'databaseName': 'GEN-UNIQUE-8', 'serverName': 'GEN-UNIQUE-8'}

params = {}
for folder in folders:
    path = bp + folder + '/azuredeploy.parameters.json'
    if not os.path.isfile(path):
        print("skipped: " + path)

    else:
        with open(path, 'r') as pf:
            j = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(pf.read())

        for param in j['parameters']:
            if param in replacements:
                j['parameters'][param]['value'] = replacements[param]

        out = json.dumps(j, indent=2)
        with open(path, 'w') as tf:
            tf.write(out)
    

    
