# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#QUIZ 6A
#QNS1
#It will produce a key value pair (i,MijVj).

# <codecell>

#QNS2
# M = xy
# N = yz
# P = M N
# key value pair of (i,k) (M,j,mij) for k = 1,2 ... up to the number of columns of N
# key value pair of (i,k),(N,j,njk) for i = 1,2 ... up to the number of rows of M

#The output of the map function has z+x different key ( z and x might have overlaps i think )  / 2y pairs with each key
#There are key-value y pairs with each key
#There 2xyz key-value pairs in all [correct]
#Reduce has 2y pairs
#The length of the value associated with each key

# <codecell>

#QNS3
#Did not attempt this qns , lazy lol...

# <codecell>

#QNS4
# Map
# For each (a,b) of R produce the key-value pair (b,(R,a))
# For each (b,c) of S produce the key-value pair (b,(S,c))
# Just find the common keys for the ans

# <codecell>

#QUIZ 6B
#Qns 1
# Let w.x + b = 0 where w = (w1,w2)
# Use solver to solve it
# 3 unknowns so 3 eqn
# 5w1 + 4w2 + b = 1
# 8w1 + 3w2 + b = 1
# 7W1 + 2w2 + b = -1
import numpy as np
A = np.matrix('5 4 1;8 3 1;7 2 1')
B = np.matrix('1;1;-1')
np.linalg.solve(A,B)

# <codecell>

#Qns 2 
import numpy as np
Label = np.matrix('1;1;1;1;0;1;1;1;0;0;0;1;0;0;0;0')
A = np.matrix('5 10;7 10;1 8;3 8;5 8; 7 8; 1 6;3 6;5 6;7 6;1 4;3 4;5 4;7 4;1 2;3 2')
W = np.matrix('-1;1')
E = A * W - 2
# 1- e iff point is +
# -1 + e iff point is -
print np.concatenate((Label,A,E),axis=1)

# <codecell>

#Qns3
buys = [(28,145), (38,115), (43,83), (50,130), (50,90), (50,60), (50,30), (55,118), (63,88),(65,140)]
donbuy = [(23,40), (25,125), (29,97), (33,22), (35,63), (42,57), (44, 105), (55,63), (55,20), (64,37)]
def tree(L):
    for i in L:
        print i
        if (i[0] < 45):
             if (i[1] < 110):
                print "Doesnt Buy"
             else:
                print "Buys"
        else:
            if (i[1] < 75 ):
                print "Doesnt Buy"
            else:
                print "Buy"

print "=Buys="
tree(buys)
print "=Don Buys="
tree(donbuy)

