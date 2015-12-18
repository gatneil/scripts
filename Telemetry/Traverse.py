from Traverser import *

root = '/home/ubuntu/azure-quickstart-templates/'

def keyFunc(filePath, fullObj, keyList):
    print(filePath + '[key]: ' + str(keyList))

def leafFunc(filePath, fullObj, keyList, val):
    print(filePath + '[leaf]: ' + str(keyList) + ' -> ' + str(val))

t = Traverser(root, keyFunc, leafFunc, False)
t.traverseRepo()





