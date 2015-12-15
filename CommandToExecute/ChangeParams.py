import simplejson as json
import collections
import os.path
from Common import *

replacements = {'storageAccountPrefix': 'GEN-UNIQUE', 'replicatorPassword': 'GEN-PASSWORD', 'newStorageAccountName': 'GEN-UNIQUE', 'storageNameForFrontEnd': 'GEN-UNIQUE', 'mySqlPassword': 'GEN-PASSWORD', 'administratorLoginPassword': 'GEN-PASSWORD', 'dnsName': 'GEN-UNIQUE', 'datastaxPassword': 'GEN-PASSWORD', 'opsCenterAdminPassword': 'GEN-PASSWORD', 'storageAccountNamePrefix': 'GEN-UNIQUE', 'adminPassword': 'GEN-PASSWORD', 'clusterName': 'GEN-UNIQUE', 'replicaSetKey': 'GEN-SSH-PUB-KEY', 'domainName': 'GEN-UNIQUE', 'dnsNameForPublicIP': 'GEN-UNIQUE', 'privateDomainName': 'GEN-UNIQUE'}

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
    

    
