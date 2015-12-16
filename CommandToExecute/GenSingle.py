import collections
import json

from Common import *

def ModifyResource(resource, origin, destination):
    if origin not in resource['properties']:
        return

    if 'commandToExecute' in resource['properties'][origin]:
        command = resource['properties'][origin]['commandToExecute']
        del resource['properties'][origin]['commandToExecute']
        if destination in resource['properties']:
            resource['properties'][destination]['commandToExecute'] = command
        else:
            resource['properties'][destination] = {'commandToExecute': command}

        if len(resource['properties'][origin]) == 0:
               del resource['properties'][origin]

def HandleBlock(templateFile, block, isResource):
    if not isResource:
        return

    if block['type'] == 'Microsoft.Compute/virtualMachines/extensions':
        if block['properties']['type'] == 'CustomScriptForLinux':
            if templateFile not in excludeFiles:
                ModifyResource(block, 'settings', 'protectedSettings')

            else:
                ModifyResource(block, 'protectedSettings', 'settings')

            block['properties']['typeHandlerVersion'] = '1.4'
    

def GenSingleHelper(templateFile, block, isResource):
    # if we are at a leaf-node (i.e. a value), return
    if (not isinstance(block, collections.Mapping)) and (not isinstance(block, list)):
        return

    # handle the current block
    HandleBlock(templateFile, block, isResource)

    # recurse through the object to find all resources
    for key in block:
        if key == "resources":
            for resource in block[key]:
                GenSingleHelper(templateFile, resource, True)
        else:
            if isinstance(block[key], list):
                for innerBlock in block[key]:
                    GenSingleHelper(templateFile, innerBlock, False)
            else:
                GenSingleHelper(templateFile, block[key], False)

def GenSingle(templateFile):
    with open(templateFile, 'r') as tf:
        template = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(tf.read())

    # initiate deep iteration through the template
    GenSingleHelper(templateFile, template, False)

    out = json.dumps(template, indent=2)
    with open(templateFile, 'w') as tf:
        tf.write(out)
