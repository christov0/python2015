#!/usr/bin/env python

import sys
import compute

if len(sys.argv) != 2:
    exit("Usage: compute_it.py <expression>")

if 'C' in compute.VALID_DNA:
    print "C is a base"
if 'D' in compute.VALID_DNA:
    print "D is a base"
else:
    print "D is not a base"

compute.hello()
print compute.compute(sys.argv[1])
