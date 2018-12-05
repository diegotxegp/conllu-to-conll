#!/usr/bin/env python
#encoding=utf-8
'''
Converter from .conllu format to .conll format for Universal Dependencies

Check if each folder has three .conllu files for train, dev and test, and if the files are properly filled (e.g.: word or lemma are _)

@author: diego.garciap
Created on 31/01/2018


Command line:

python conllu-to-conll-standard.py #<origin path> #<destination path>
'''

import sys

#
with open(sys.argv[1].strip(),'r') as conllu, open(sys.argv[2].strip(),'w') as conll:

    lines=conllu.readlines()

    for line in lines:
        tupl = line.split()

        if len(tupl)==10 and tupl[0]!='#' and '.' not in tupl[0] and '-' not in tupl[0]:
            tupl[8] = tupl[9] = '_'
            conll.write('\t'.join(tupl)+'\n')
        if len(tupl)==0:
            conll.write('\n')
