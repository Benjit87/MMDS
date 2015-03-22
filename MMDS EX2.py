# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Quiz2A
#Question 1
#Lecture did not cover the algorithm, the code is from someone from http://rosettacode.org/wiki/Longest_common_subsequence#Python alterantively you can use some standard libraries 
def lcs(xstr, ystr):
    """
    >>> lcs('thisisatest', 'testing123testing')
    'tsitest'
    """
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

#he, she, his, and hers
#he she
#he his
#he hers
#she his
#she hers
#his hers
import itertools
words = ("he","she","his","hers")
wordCombination = itertools.combinations(words,2)
for pairs in wordCombination:
    print pairs , ":" , len(pairs[0])+len(pairs[1]) - 2 * len(lcs(pairs[0],pairs[1]))

# <codecell>

#Question 2
import numpy as np
#Matrix
#M = np.matrix("1 0 1 0;1 0 0 1;0 1 0 1;0 1 0 1;0 1 0 1;1 0 1 0;1 0 1 0")
M = np.matrix("0 1 1 0;1 0 1 1;0 1 0 1;0 0 1 0;1 0 1 0;0 1 0 0")
#Signature
S = np.matrix("0 0 0 0")
#Order = (5,6,1,2,6,4,3)
Order = (4,6,1,3,5,2) 
def minHash(M,S,Order):
    for i,counter in zip(Order,range(M.shape[0]-1)):
        for j in range(M.shape[1]):
            if M[i-1,[j]] == 1 and S[0,[j]] == 0:
                S[0,[j]] = Order[counter]
    return S
#Minhaash at the Row Id
# R5 R6 R4 R3
print minHash(M,S,Order)

# <codecell>

#Question 3
import numpy as np
M = np.matrix("1 2 1 1 2 5 4;2 3 4 2 3 2 2;3 1 2 3 1 3 2;4 1 3 1 2 4 4;5 2 5 1 1 5 1;6 1 6 4 1 1 4")
dict1 = {}
for i in range(3):
    for j in range(M.shape[1]):
        if dict1.has_key(str(M[(i)*2:((i+1)*2),j])):
           dict1[str(M[(i)*2:((i+1)*2),j])] = dict1[str(M[(i)*2:((i+1)*2),j])] + "|" + "B" + str(i+1) + "C" + str(j+1)
        else:
           dict1[str(M[(i)*2:((i+1)*2),j])] = "B" + str(i+1) + "C" + str(j+1)

            
dict1   
#Find those pairs that appear in >= 1 Band

# <codecell>

#Question 4
t1 = "ABRACADABRA"
list1 = []
for i,j in zip(t1,t1[1:]):
    list1.append(str(i) + str(j))

#2 shingles
print len(list1)
t2 = "BRICABRAC"
list2 = []
for i,j in zip(t2,t2[1:]):
    list2.append(str(i) + str(j))
#2 shingles
print len(list2)

#Jaccard Similarity
print len(set(list1).intersection(list2)) , "/" , len(set(list1).union(set(list2)))

# <codecell>

#Question 6

list1 = [(61,8),(58,13),(55,5),(63,8)]
for i in list1:
    if (i[0]+i[1] < abs(i[0] - 100) + abs(i[1] - 40)) and (i[0]*i[0] + i[1]*i[1] > (i[0]-100)*(i[0]-100)+(i[1]-40)*(i[1]-40)):
        print i

# <codecell>

#Quiz 2B
#Question 1
import math
#Either a triangular matrix (n)(n-1) / 2 or a hash table 2M for 2nd pass
def qns1(N,M,S):
    triangle = (N*N-1/2)*4
    hashtable = 2 * M * 4
    print "triangle/S" , triangle/float(S)
    print "hashtable/S" , hashtable/float(S)
    print "S",S
 
qns1(30000,200000000,1800000000)
qns1(30000,100000000,500000000)
qns1(40000,200000000,3200000000)
qns1(50000,80000000,1500000000)


# <codecell>

#Qns2
#Item i is in basket j iif j/i
#i is a mutiple of j
#100% confidence means support(LHS U RHS) / support(LHS)
dict = {}
for j in range(1,100+1):
    list = []
    for i in range(1,j+1):
        if ((j)%(i) == 0):
            list.append(i)
    dict[j] = list
dict

#From the 4 options the common mutiple of 12 and 18 only 36
#12 and 18 also did not appear in other basket from 1 to 100 together except for basket 36,72 which also includes 36

# <codecell>

#Question3
#An itemset that is not frequent might have frequent or nonfrequent subset

# <codecell>

#Quiz2C
#Question1
#No Idea, See discussion forum for expert replies
#1st pass size of bucket pairs + count
#Bitmap of 2nd pass P/32 pairs in bucket 12 bytes per pairs
import math
S = 200000000
P = 1600000000
def qns2c(S,P):
    
    return (1000000 * 12.0) + P / S
print qns2c(100000000,200000000)
print qns2c(300000000,750000000)
print qns2c(500000000,10000000000)
print qns2c(200000000,400000000)

print 1800000000/300000000

# <codecell>

#Question2
#Toivonnen
#Itemset {A,B,C,D,E,F,G,H}
#Frequent Itemset {A,B}, {A,C}, {A,D}, {B,C}, {E}, {F}
#Negative border is not frequent and its subset are
#Just find answer which consist of frequent and not frequent subsets or not frequent subsets

