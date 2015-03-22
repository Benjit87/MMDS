# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Week 3A
#Qns 1
# ABCDEFGH
#A00100100
#B00001001
#C10010100
#D00101010
#E01010001
#F10100010
#G00010101
#H01001010
import numpy as np

A = np.matrix("""0 0 1 0 0 1 0 0;
                 0 0 0 0 1 0 0 1;
                 1 0 0 1 0 1 0 0;
                 0 0 1 0 1 0 1 0;
                 0 1 0 1 0 0 0 1;
                 1 0 1 0 0 0 1 0;
                 0 0 0 1 0 1 0 1;
                 0 1 0 0 1 0 1 0""")
#Sum of entries
#print np.sum(A) / 2

D = np.matrix("""2 0 0 0 0 0 0 0;
                 0 2 0 0 0 0 0 0;
                 0 0 3 0 0 0 0 0;
                 0 0 0 3 0 0 0 0;
                 0 0 0 0 3 0 0 0;
                 0 0 0 0 0 3 0 0;
                 0 0 0 0 0 0 3 0;
                 0 0 0 0 0 0 0 3""")
L = D - A


count = 0
for i in range(8):
    for j in range(8):
        if ( D[i,[j]] != 0 ):
            count = count + D[i,[j]]
print count

# <codecell>

#Qns2
#I used MatLab Eigen Computation... Python ones like giving me rubbish...
#123456
#1011000
#2100101
#3100100
#4011010
#5000101
#6010010
from scipy import linalg as LA
A = np.matrix("""0 1 1 0 0 0;
                 1 0 0 1 0 1;
                 1 0 0 1 0 0;
                 0 1 1 0 1 0;
                 0 0 0 1 0 1;
                 0 1 0 0 1 0""")
D = np.matrix("""2 0 0 0 0 0;
                 0 3 0 0 0 0;
                 0 0 2 0 0 0;
                 0 0 0 3 0 0;
                 0 0 0 0 2 0;
                 0 0 0 0 0 2""")
L = D - A
e_vals, e_vecs = np.linalg.eig(L)
eigvals = np.round(e_vals,2)
eigvecs = np.round(e_vecs,2)
print np.mean(eigvecs[:,4])

#Take the 2nd column of the vector and split by mean
#mean = np.mean(e_vecs[:,1])
#print mean
#print e_vecs
#print e_vecs[:,1] - mean
#print e_vecs[:,1] > mean

#Matlab is F,T,F,F,T,T
print e_vecs
print eigvecs
print np.round(e_vecs[:,4],2)

# <codecell>

#Qns3
#from timestamp 1 to 70 each appear 7 times except for number 1 2 3 4 5
#Surprise
S = 5*7*7 + 5*8*8

#number of times it occur from 31 to 75
def moment2(A,S):
    X1 = A[0]%10
    X1Value=0
    for i in range(A[0],76):
        if i%10 == X1:
            X1Value = X1Value + 1
    X2 = A[1]%10
    X2Value=0
    #number of times it occur from 31 to 75
    for i in range(A[1],76):
        if i%10 == X2:
            X2Value = X2Value + 1
    X3 = A[2]%10
    X3Value=0
    #number of times it occur from 31 to 75
    for i in range(A[2],76):
        if i%10 == X3:
            X3Value = X3Value + 1
    print X1Value,X2Value,X3Value
    return (75.0/3*(X1Value*2-1 + X2Value*2-1 + X3Value*2-1))/S

#OptionABCD
print moment2((31, 32, 44),S)
print moment2((24, 44, 65),S)
print moment2((30, 47, 62),S)
print moment2((4, 31, 72),S)

# <codecell>

#Question4
#Flagolet-Martin algorithm find closest to estimate 4
def hasf(x):
    return bin((3 * x + 7 ) % 11)
#Count trailing zero from the left
def countZero(x):
    x = x[::-1]
    count = 0
    for i in x:
        if i == '0':
            count = count + 1
        elif i == '1' or i == 'b':
            break;
    
    return (count) 
def qns4(l):
    
    count = -1
    #Get the Maximum Trailing Zero
    for i in l:
         
        if countZero(hasf(i)) > count:
            
            count = countZero(hasf(i))
    return pow(2,count)


print qns4((1, 3, 9, 10))
print qns4((3, 7, 8, 10))
print qns4((3, 4, 8, 10))
print qns4((2, 4, 6, 10))

 

# <codecell>

#Question5
#Draw by hand
End Time |105|104|102|95 ...
Size     |1  |2  |4  |8  ...

# <codecell>

#Week3B
#Question 1
#Go read 4.3.3 of the book
#Probability of any one element not hasing to a particular bit is 1 - 1/99
#Probabilty that 20 element not hashing to a bit (1-1/99)^20 = ( 1 - 1/99 ) ^ (99*20/99) = e ^ -20/99 (Assume 99 is large enough)
#P of 20 element hashing to a bit = 1 - e ^ -20/99

#Question 2
#
# (t+1)/10^6 fraction of users selected
# (t+1)/10^6 * 10^8 users will be selected
# n/10^8 number of email in the stream for each users
# n/10^8 * 100 number of email space consumed for each users
# ((t+1)/10^6 * 10^8) * (n/10^8*10) must be less than 10^10

def space(n,t):
    s = (t+1.0)/(pow(10,6)) * pow(10,8) * n / pow(10,8) * 100
    print s/pow(10,10)
    
space(pow(10,11),999)
space(pow(10,9),999)
space(pow(10,13),99)
space(pow(10,9),1000)

