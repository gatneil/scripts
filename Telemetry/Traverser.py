import os
import json
import collections

class Traverser:
    # keyFunc(filePath, fullObj, keyList) takes in the filepath for a
    # full template object with a
    # list of nested keys to indicate where we currently
    # are in the traversal; it is called on only non-leaf nodes

    # leafFunc(filePath, fullObj, keyList, value) takes in the filepath for a
    # full template object with a
    # list of nested keys to indicate where we currently
    # are in the traversal, and the value at that nested key path;
    # it is called on only leaf nodes

    # root must end in a '/'
    def __init__(self, root, keyFunc, leafFunc, debug):
        self.root = root
        self.keyFunc = keyFunc
        self.leafFunc = leafFunc
        self.debug = debug

    def fileFilter(self, f):
        return 'json' in f and 'parameters' not in f and 'metadata' not in f and 'UiDefinition' not in f
    
    def traverseRepo(self):
        # get actual subdirectories, not files
        subdirs = [fsobj for fsobj in os.listdir(self.root) if '.' not in fsobj]

        for subdir in subdirs:
            fullPath = self.root + subdir
            self.traverseTopLevelFolder(fullPath)

    def traverseTopLevelFolder(self, topLevelDirPath):
        jsonFiles = []
        walk = os.walk(topLevelDirPath)
        for level in walk:
            for f in level[2]:
                fullPath = level[0] + '/' + f
                jsonFiles.append(fullPath)

        deploymentFiles = [f for f in jsonFiles if self.fileFilter(f)]

        if self.debug:
            print('deployment files for ' + topLevelDirPath + ': ' + str(deploymentFiles))

        for deploymentFile in deploymentFiles:
            self.traverseFile(deploymentFile)

    def traverseFile(self, deploymentFile):
        with open(deploymentFile, 'r') as tf:
            # use OrderedDict to preserve order of keys in case we want to
            # write them back out in the same order as they were read in
            try:
                template = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(tf.read())
            except:
                print('couldn\'t JSON decode file ' + deploymentFile + '. Please check that the file is valid JSON. Skipping for this run.')
                return

        self.traverseFileHelper(deploymentFile, template, [])
                           
        
    def traverseFileHelper(self, filePath, template, keyList):
        node = self.getNested(keyList, template)
        if isinstance(node, collections.Mapping) or isinstance(node, list):
            # non-leaf node
            self.keyFunc(filePath, template, keyList)
            
            if isinstance(node, collections.Mapping):
                for key in node:
                    self.traverseFileHelper(filePath, template, keyList + [key])

            elif isinstance(node, list):
                l = len(node)
                for i in xrange(0, l):
                    self.traverseFileHelper(filePath, template, keyList + [i])

            else:
                assert(0)

        else:
            # leaf-node; no need to recurse
            self.leafFunc(filePath, template, keyList, node)
        

    # gets the value of col[keyList[0]][keyList[1]]...[keyList[-1]]
    def getNested(self, keyList, col):
        return reduce(lambda subCol, key: subCol[key], keyList, col)
        
