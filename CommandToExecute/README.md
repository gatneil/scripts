OVERVIEW
========
All scripts are idempotent.

Common.py has the list of folders that the scripts operate on.

Find.py has the FindFiles function that returns all json files that actually deploy resources (e.g. not parameter files, metadata files, or createUiDef files).


USEFUL COMMANDS
===============
python Gen.py: moves "commandToExecute" from "settings" to "protectedSettings" for all VM extensions

python FindParams.py: prints out a list of params; useful for figuring out what params should use what Travis CI special values

python ChangeParams.py: inserts Travis CI special values based on the dict at the top of the file

DEBUGGING
=========

ValueError: No JSON object could be decoded -> if you run into this error, try replacing "import json" with "import simplejson as json" at the top of the file and try again; this should give better error messages. Generally, this is because the script is trying to read in a file that doesn't exist.