'''
    Author: Lasantha Samarakoon
    Description: Checkouts a Git tag as a new branch with the same tag name.
    Usage: python gitcotag.py <TAG_NAME>
'''

import subprocess
import sys

if (len(sys.argv) == 2):
    tag = sys.argv[1]
    print(tag)
    command = 'git checkout tags/{0} -b {1}'.format(tag, tag)
    subprocess.call(command, shell=True)
else:
    print('Usage: python gitcotag.py <TAG_NAME>')
    sys.exit(1)