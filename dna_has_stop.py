# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:46:26 2015

@author: tedscott
"""
# define has_stop function here
def has_stop(dna,frame=0) :
    "This function returns true if the input string contains a stop codon"
    stop_codon_found=False
    # create list of stop codons
    stop_list=['tga','tag','taa']
    for i in range(frame,len(dna),3) :
        codon=dna[i:i+3].lower()
        if codon in stop_list:
            stop_codon_found=True
            break
    return stop_codon_found 

def rev_complement(dna) :
    seq=reverse(dna)
    seq=complement(dna)
    return seq
    
def reverse(seq) :
    new_seq=seq[::-1]
    return new_seq
    
def complement(seq) :
    basecomplement={"a":"t","c":"g","t":"a","g":"c"}
    letters=list(seq)
    letters=[basecomplement[base] for base in letters]
    return ''.join(letters)
    
def foo() :
    print("foo")
    
    