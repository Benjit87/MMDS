# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Week4A
#Qns1
import numpy as np

M = np.matrix('1 2 3 4 5;2 3 2 5 3;5 5 5 3 2')
rowMean = np.mean(M,axis=1)
M = M-rowMean
colMean = np.mean(M,axis=0)
M = M - colMean
print M

# <codecell>

#Qns2
#See example 9.2 of Chapter 9
Ma = np.matrix('1.0 0 1 0 1 2;1 1 0 0 1 6;0 1 0 1 0 2')
def cosine(M,alpha):
    M[:,[5]] = M[:,[5]]*alpha
    print M
    print "Alpha = ",alpha
    print "sim(A,B)"
    numerator = (M[0,:] * M[1,:].transpose()).flat[0]
    denomerator = np.sqrt((M[0,:] * M[0,:].transpose()).flat[0]) * np.sqrt((M[1,:] * M[1,:].transpose()).flat[0])
    print numerator/denomerator
    print "sim(A,C)"
    numerator = (M[0,:] * M[2,:].transpose()).flat[0]
    denomerator = np.sqrt(M[0,:] * M[0,:].transpose()).flat[0] * np.sqrt(M[2,:] * M[2,:].transpose()).flat[0]
    print numerator/denomerator
    print "sim(B,C)"
    numerator = (M[1,:] * M[2,:].transpose()).flat[0]
    denomerator = np.sqrt(M[1,:] * M[1,:].transpose()).flat[0] * np.sqrt(M[2,:] * M[2,:].transpose()).flat[0]
    print numerator/denomerator

cosine(Ma,0)

# <codecell>

#Week4B
#Question 1
#Length of vector must be 1 and dot product must be 0
M = np.matrix([2/7.0, 3/7.0, 6/7.0])
print M * np.matrix('-.937, .312, .156').transpose()
print M * np.matrix('2.250, -.500, -.750').transpose()
print M * np.matrix('.429, .857, .286').transpose()
print M * np.matrix('-.288, -.490, .772').transpose()

#print np.matrix('.485, -.485, .728') * np.matrix('-.297, .890, -.346').transpose()

# <codecell>

#Question 2
#Do by hand easier
#2x +3y +6z = 0 => 2x = -3y -6z (1)
#6x +2y -3z = 0 (2)
#Sub 1 into 2
#-9y -18z + 2y -3z  = 0 => -21z - 7y = 0 => y =-3z

# <codecell>

#Question 3
M = np.matrix('1 1;2 2;3 4').transpose()
print M * M.transpose()


# <codecell>

#Question 4
A = np.matrix('1 ;2; 3')
np.matrix([1, -2, 1]) * A

