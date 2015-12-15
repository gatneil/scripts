import collections
import json

def GenSingle(templateFile):
    with open(templateFile, 'r') as tf:
        template = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(tf.read())

    for resource in template['resources']:
        if resource['type'] == 'Microsoft.Compute/virtualMachines/extensions':
            if resource['properties']['type'] == 'CustomScriptForLinux':
                if 'commandToExecute' in resource['properties']['settings']:
                    command = resource['properties']['settings']['commandToExecute']
                    del resource['properties']['settings']['commandToExecute']
                    resource['properties']['protectedSettings'] = {'commandToExecute': command}

                resource['properties']['typeHandlerVersion'] = '1.4'
        

    out = json.dumps(template, indent=2)
    with open(templateFile, 'w') as tf:
        tf.write(out)
