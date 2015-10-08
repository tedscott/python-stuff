# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:19:31 2015

@author: tedscott
"""

def get_extension1(filename):
    return(filename.split(".")[-1])
    
def get_extension2(filename):
    import os.path
    return(os.path.splitext(filename)[1])
    
def get_extension3(filename):
    return filename[filename.rfind('.'):][1:]
    
    
fasta_string="TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG"

from Bio.Blast import NCBIWWW
result_handle=NCBIWWW.qblast("blastn","nt",fasta_string)
from Bio.Blast import NCBIXML
blast_record=NCBIXML.read(result_handle)
len(blast_record.alignments)
e_thresh=0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect <= e_thresh:
            print("*** ALIGNMENT ***")
            print("Sequence: ", alignment.title)
            print("Length: ", alignment.length)
            print("e-value: ", hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)