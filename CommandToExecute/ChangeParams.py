import simplejson as json
import collections
import os.path
from Common import *

replacements = {'storageAccountPrefix': 'GEN_UNIQUE', 'replicatorPassword': 'GEN_PASSWORD', 'newStorageAccountName': 'GEN_UNIQUE', 'storageNameForFrontEnd': 'GEN_UNIQUE', 'mySqlPassword': 'GEN_PASSWORD', 'administratorLoginPassword': 'GEN_PASSWORD', 'dnsName': 'GEN_UNIQUE', 'datastaxPassword': 'GEN_PASSWORD', 'opsCenterAdminPassword': 'GEN_PASSWORD', 'storageAccountNamePrefix': 'GEN_UNIQUE', 'adminPassword': 'GEN_PASSWORD', 'clusterName': 'GEN_UNIQUE', 'replicaSetKey': 'GEN_SSH_PUB_KEY', 'domainName': 'GEN_UNIQUE', 'dnsNameForPublicIP': 'GEN_UNIQUE', 'privateDomainName': 'GEN_UNIQUE'}

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
    

    
