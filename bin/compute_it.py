#!/usr/bin/env python

import sys
from compute import *

if len(sys.argv) != 2:
    exit("Usage: compute_it.py <expression>")

#if 'C' in VALID_DNA:
#    print "C is a base"
#if 'D' in VALID_DNA:
#    print "D is a base"
#else:
#    print "D is not a base"

#hello()
print compute(sys.argv[1])
#print sys.path
