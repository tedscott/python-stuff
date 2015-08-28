# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:58:09 2015

@author: tedscott
"""
from time import clock
def timer(myfunc,dna,base):
    start=clock()
    myfunc(dna,base)
    end=clock()
    return (end-start)

def count1(dna, base):
    i = 0
    for c in dna:
        if c == base:
            i += 1 
    return i

def count2(dna, base):
    i = 0 
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1 
    return i

def count3(dna, base):
    match = [c == base for c in dna]
    return sum(match)

def count4(dna,base): return dna.count(base)
    
def count5(dna,base):return len([i for i in range(len(dna)) if dna[i] == base])

def count6(dna,base): return sum(c == base for c in dna)

import random
def create_dna(n, alphabet="acgt"):
    return ''.join([random.choice(alphabet) for i in range(n)])
    
def function1(length):
    if length > 0:
        print(length)
        function1(length - 1)

def function2(length):
    while length > 0:
        print(length)
        function2(length - 1)
        
def compute(n,x,y):
    if n==0 : return x
    return compute(n-1,x+y,y)
    
def valid_dna3(dna):
    for c in dna:
        flag = c in 'acgtACGT'
    return flag
    
def valid_dna1(dna):
    for c in dna:
        if c in 'acgtACGT':
            return True
        else:
            return False

def f(mystring):
         print(message)
         print(mystring)
         message="Inside function now!"
         print(message)
         
def open_fasta(filename):
    """opens a file and reads dna sequences"""
    try:
        f=open(filename)
    except IOError:
        print("could not open the file")
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
    
for name,seq in thing.items():
    print(name,seq)
    
    
    
import subprocess
subprocess.call(["notepad.exe"]) # start notepad