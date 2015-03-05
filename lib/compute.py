#!/usr/bin/env python

VALID_DNA = ('A','C','T','G','N')

def compute(astring):
    expression_list = astring.split()
    total = float(expression_list[0])
    operation = ''
    for element in expression_list[1:]:
        if element == '+':
            operation = element
        else:
            total += float(element)
    return total

def hello():
    print "Hello World"

if __name__ == "__main__":
    print "I am running as a script"
