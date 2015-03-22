# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Question 1
import numpy as np

M = np.matrix([[0,0,0],[0.5,0,0],[0.5,1,1]])
r = np.matrix([[1.0],[1.0],[1.0]])

def powerIter(M,r1,B):
    e = r1
    ran = r1
    while ((e > 0.01).all()):
        r2 = (B * M) * r1 + (1-B) * ran   
        e =  r1 - r2
        r1 = r2
	return r2

powerIter(M,r,0.7)

# <codecell>

#Question 2

A = (0.85) C + 0.05A + 0.05B + 0.05C
B = (0.85)( 0.5A ) + 0.05A + 0.05B + 0.05C
C = (0.85)( 0.5A + B ) + 0.05A + 0.05B + 0.05C

# <codecell>

#Question 3

M = np.matrix([[0,0,1],[0.5,0,0],[0.5,1,0]])
r = np.matrix([[1.0],[1.0],[1.0]])

def powerIter(M,r1,i):
    for x in range(0,i):
        r2 = M * r1 
        r1 = r2
    return r2

powerIter(M,r,4)

# <codecell>

#Question4
set1 = []
dict1 = {}
y = 10

def map(y):
    for x in range(1,y):
        if y % x == 0:
            set1.append((x,y))
        

map(15)
map(21)
map(24)
map(30)
map(49)

def reduce(set):
    for x in set:
        if dict1.has_key(x[0]):
            dict1[x[0]] = dict1[x[0]] + x[1]
        else:
            dict1[x[0]] = x[1]

reduce(set1)
dict1

