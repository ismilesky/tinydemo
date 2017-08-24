__author__ = 'wslhk'

import tinify
import os
import sys

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# APIKEY
tinify.key = "FGMDMXdQ6dtNo0NFN1dPUGQ-1SSFpVZH"

folderinput=sys.argv[1]
if folderinput =='':
 folderinput='./input'

files = os.listdir(folderinput)
ouputpath=folderinput+"/output/"
if(os.path.exists(ouputpath)==False):
    os.mkdir(folderinput+"/output/")

for filename in files :
    if '.png' in filename:
        source = tinify.from_file(folderinput+"/"+filename)
        source.to_file(folderinput+"/output/"+filename)
    pass

print('successful')
