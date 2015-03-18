#!/usr/bin/env python

import sys

def split_fasta(filename, num_parts=2):
    try:
        input_file = open(filename)
    except IOError as e:
        print >>sys.stderr, "Failed to open {}: {}".format(filename, e.strerror)
        return False
    else:
        output_files = []
        count = 0
        with input_file:
            for line in input_file:
                if line.startswith('>'):
                    count += 1
                    filenum = (count - 1) % num_parts
                    if len(output_files)-1 < filenum:
                        filename = 'seq{}.fasta'.format(filenum+1)
                        output_file = open(filename, 'w')
                        output_files.append(output_file)
                    else:
                        output_file = output_files[filenum]
                output_file.write(line)
        for output_file in output_files:
            output_file.close()
        if count < num_parts:
            print >>sys.stderr, "Warning: number of parts ({}) is greater than number of sequences in file ({})".format(num_parts, count)
            return False        
        return True

if __name__ == '__main__':
        if len(sys.argv) != 3:
                sys.exit("Usage: split_fasta.py <FASTA filename> <number of parts")

        filename = sys.argv[1]
        num_parts = int(sys.argv[2])
        if split_fasta(filename, num_parts):
                sys.exit(0)
        else:
                sys.exit(1)
