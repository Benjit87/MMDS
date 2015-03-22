# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Quiz 7A
#Did not attempt this advance quiz

#Quiz 7B
#Qns1
#  1   2 3 4 
#1 0   1 0 0
#2 0.5 0 0 0
#3 0.5 0 0 1
#4 0   0 1 0
import numpy as np

M = np.matrix([[1,0,0,0],[0.5,0,0,0],[0.5,0,0,1],[0,0,1,0]])
r = np.matrix([[1/4.0],[1/4.0],[1/4.0],[1/4.0]])

def powerIter(M,r1,B):
    e =  np.matrix([[1.0],[1.0],[1.0],[1.0]])
    ran = np.matrix([[2],[1],[0],[0]])
    while ((e > 0.01).all()):
    
        r2 = (B * M) * r1 + (1-B) * ran   
        
        e =  r1 - r2
        r1 = r2
	return r2

print powerIter(M,r,0.7)

# <codecell>

#Qns2
#Read Section 5.4.1 of the book

