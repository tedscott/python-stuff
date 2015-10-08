# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:15:38 2015

@author: tedscott
"""
# here is the sequence
dna='acgtgctgtatgctgatgctgatgcgcgctgatcgtagtcgtagctagtttttcgagtat'
no_c=dna.count('c') #count of c's
no_g=dna.count('g') #count of g's
dna_len=len(dna) # get length of dna
gc_percent=(no_c+no_g)*100/dna_len
print(gc_percent)


if 'l' in dna or 'L' in dna:
    num_ls=dna.count('l')+dna.count('L')
    print("the number of l chars is %d" % num_ls)
if 'a' in dna or 'A' in dna:
    num_as=dna.count('a')+dna.count('A')
    print("the number of a chars is %d" % num_as)
else:
    print("there were no a or l chars in dna")  
    
N=25
for i in range(2,N):
    for j in range(2,i):
        if i%j==0:
            print(i," equals ",j," * ",i//j)
            break #not a prime number
    else:
        print(i," is prime!")
        

while i< 2048 :
      i=2*i
      print(j)
      j=j+1
     
seq="food is food"
for i in range(len(seq)+1) :    # line 1 
        for j in range(i) :        # line 2 
                print(seq[j:i])     # line 3      
                

d = {}
result = False
for x in mylist:
       if not x in d:
           d[x]=True
           continue
       result = True      
       
def funky(a) :
    "this function is funky"
    print("the value of %s is %d" %(a,int(a))
    return a
    
def gc(dna) :
    "this function computes the gc % of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent
    
    
                
        