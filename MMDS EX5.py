# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Quiz5A
#Qns1
#This is actually for Week4 CUR Algorithm
import numpy as np
#Get the SVD
M = np.matrix('1 0 0;0 2 0;0 0 0')
#Construct the diagonal U
a,U,c = np.linalg.svd(M)
U = np.diag(U)
#Inv it
ans = np.linalg.pinv(U)
print ans

# <codecell>

#Qns2
CTR = [0,0,0,0,0]
B = [1,2,3,4,5]
P = [0.1, 0.09, 0.08, 0.07, 0.06]
M = np.matrix('0.015 0.010 0.005;0.016 0.012 0.006;0.017 0.014 0.007;0.018 0.015 0.008;0.019 0.016 0.010')
#Expected yield
E = np.diag(P) * M

#Phase1
def phase():
    while sum(CTR) < 101 and sum(B) > 0:
        #1st column
        r1 = np.argmax(E[:,0] == np.max(E[:,0]))
        if B[r1] != 0:
            B[r1] = B[r1] - P[r1]
            CTR[r1] = CTR[r1] + 1
        if B[r1] - P[r1] < 0:
            B[r1] = 0
            E[r1,0] = -1
             
        #2nd Column
        #Temp E
        T = E
        T[r1,1] = -1
        r2 = np.argmax(T[:,1] == np.max(T[:,1]))
        if B[r2] != 0:
            B[r2] = B[r2] - P[r2]
            CTR[r2] = CTR[r2] + M[r2,1]/M[r1,0]
        if B[r2] - P[r2] < 0:
            B[r2] = 0
            E[r2,0] = -1        
        #3rd Column
        T[r1,2] = -1
        T[r2,2] = -1
        r3 = np.argmax(T[:,2] == np.max(T[:,2]))
        if B[r3] != 0:
            B[r3] = B[r3] - P[r3]
            CTR[r3] = CTR[r3] + M[r3,2]/M[r1,0]
    
        if B[r3] - P[r3] < 0:
            B[r3] = 0
            E[r3,0] = -1
        if B[r1] == 0 or B[r2] == 0 or B[r3] == 0:
            break
    for i in range(0,5):
        CTR[i] = round(CTR[i])
#Phase1
phase()
print B
print CTR
print "==="
#Phase2
phase()
print B
print CTR
print "==="
#Phase3
phase()
print B
print CTR
print "==="

# <codecell>

#Qns3
import sys
added = [ (0,0), (10,10) ]
p = [ (1,6), (3,7), (4,3), (7,7), (8,2), (9,5) ]
while p != []:
    dist1 = 0
    maxpoint = None
    for i in p:
        dist2 = sys.maxint
        minpoint = None
        for j in added:
            test =  pow(j[0]-i[0],2) + pow(j[1]-i[1],2)
            if dist2 > pow(j[0]-i[0],2) + pow(j[1]-i[1],2):
                minpoint = i
                dist2 = pow(j[0]-i[0],2) + pow(j[1]-i[1],2)
            #print i
            #print test
       
        if ( maxpoint == None or dist2 > dist1):
            dist1 = dist2
            maxpoint = minpoint
        #print "mindist",minpoint
        #print "minpoint",dist2
        #print dist1
        #print maxpoint
    p.remove(maxpoint)
    added.append(maxpoint)
print added          
    

# <codecell>

#Quiz5B
import sys
C = [(25,125), (44,105), (29,97), (35,63), (55,63), (42,57), (23,40), (64,37), (33,22), (55,20)]
P = [(28,145), (50,130), (65,140), (38,115), (55,118), (50,90), (63,88), (43,83), (50,60), (50,30)]
P2 = []
for i in range(0,10):
    mindist = sys.maxint
    mp = None
    for j in range(0,10):
        dist = pow(C[j][0]-P[i][0],2) + pow(C[j][1]-P[i][1],2)
        if dist < mindist:
            mp = j
            mindist = dist
    P2.append(mp)
#Recompute Centroid
C2 = C
for i,j in zip(P2,range(0,10)):
    C2[i] = ((P[j][0] + C2[i][0], P[j][1] + C2[i][1]))
D = np.ones(10)
for i in P2:
    D[i] += 1
for i in range(0,10):
    C2[i] = (C2[i][0]/D[i],C2[i][1]/D[i])

#Computed Centroid
print C2
#Compute nearest centroid
P3 = []
for i in range(0,10):
    mindist = sys.maxint
    mp = None
    for j in range(0,10):
        dist = pow(C2[j][0]-P[i][0],2) + pow(C2[j][1]-P[i][1],2)
        if dist < mindist:
            mp = j
            mindist = dist
    P3.append(mp)
print P3

# <codecell>

#Qns2
#for yellow distance to a,b must be lesser den to c,d 
YPUL = (6,7)
YPLR = (11,4)
BPUL = (14,10)
BPLR = (23,6)
#yellow
ULYdist = pow(5-YPUL[0],2) + pow(10-YPUL[1],2)
LRYdist = pow(5-YPLR[0],2) + pow(10-YPLR[1],2)
print ULYdist
print LRYdist
#blue
ULBdist = pow(20-YPUL[0],2) + pow(5-YPUL[1],2)
LRBdist = pow(20-YPLR[0],2) + pow(5-YPLR[1],2)
print ULBdist
print LRBdist
print ULYdist < ULBdist and LRYdist < LRBdist
print "----"
#yellow
ULYdist = pow(5-BPUL[0],2) + pow(10-BPUL[1],2)
LRYdist = pow(5-BPLR[0],2) + pow(10-BPLR[1],2)
print ULYdist
print LRYdist
#blue
ULBdist = pow(20-BPUL[0],2) + pow(5-BPUL[1],2)
LRBdist = pow(20-BPLR[0],2) + pow(5-BPLR[1],2)
print ULBdist
print LRBdist
print ULYdist > ULBdist and LRYdist > LRBdist

# <codecell>

#Qns3
#A bid on x and y
#B bid on x and z
#Just find the most approriate one using Balance algorithm

# <codecell>

#Qns4
#Dumb: Select sets for the collection in the order in which they appear on the list. Stop when all element are covered
#AB BC CD DE EF FG GH 
print 7/4.0
#Simple: Consider sets in the order in which they appear on the list.
#       When it is considered, select a set if it has at least one element that is not already covered. 
#       Stop when all elements are covered
#AB BC CD DE EF FG GH  
print 7/4.0
#Largest-First: Consider sets in order of their size. If there are ties, 
#               break the tie in favor of the one that appears first on the list. 
#               When it is considered, select a set if it has at least one element that is not already covered.
#               Stop when all elements are covered
#ADG ADF AB BC DE GH
print 6/4.0
#Most-Help: Consider sets in order of the number of elements they contain that are not already covered.
#           If there are ties, break the tie in favor of the one that appears first on the list. 
#           Stop when all elements are covered. 
#ADG BC EF GH 
print 4/4.0

# <codecell>

#Qns5
#1st perfect matching
a0,b1
a1,b3
a2,b0
a3,b2
a4,b4
#2nd perfect matching
a0,a0
a1,b2
a2,b4
a3,b1
a4,b3

