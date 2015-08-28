# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:10:04 2015

@author: tedscott

processfasta.py takes in a fasta file and outputs a dictionary with all 
the DNA sequences within the file
"""

import sys
import getopt

def usage():
    print
    """this program does stuff! It reads in a FASTA file and builds
    a dict with all sequences larger than the parameter specified for l
    
    processfasta.py [-h] [-l <length>] <filename.fa>
    
    -h              print this message
    -l <length>     only include seqs of length > this value
                    default <length> = 0
    filename        must be in FASTA format
    """
    
o,a = getopt.getopt(sys.argv[1:],'l:h')
opts={} # empty dict
seqlen=0 # default value for length filter

for k,v in o:
    opts[k]=v
    
if 'h' in opts.keys():
    usage();sys.exit()
    
if len(a) < 1:
    usage();sys.exit("fasta file not included as argument")
if 'l' in opts.keys():
    if opts['l']<0:
        print("length of sequence paramenter mut be positive");sys.exit(0)
    seqlen=opts['l']

filename=sys.argv[1]

#opens a file and reads dna sequences
try:
    f=open(filename)
except IOError:
    print("could not open the file %s" % filename)
seqs={}

for line in f:
    # discard newline chars
    line=line.rstrip()
    #distinguish header from sequence
    if line.startswith('>'):
        words=line.split() #break into words
        name=words[0][1:] # grab first word and drop first character '>'
        seqs[name]='' #currently only have ID and not the sequence
    else: #we have the sequence, not the header
        seqs[name]=seqs[name]+line
f.close()
return seqs