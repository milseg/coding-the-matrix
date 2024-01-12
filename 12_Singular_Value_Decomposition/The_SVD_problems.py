# version code 0caa61797a35+
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec
from math import sqrt
from matutil import listlist2mat


## 1: (Problem 11.8.1) Procedure for computing squared Frobenius norm
def squared_Frob(A):
    '''
    Computes the square of the frobenius norm of A.

    Example:
    >>> squared_Frob(Mat(({1, 2}, {1, 2, 3, 4}), {(1, 1): 1, (1, 2): 2, (1, 3): 3, (1, 4): 4, (2, 1): -4, (2, 2): 2, (2, 3): -1}))
    51
    '''
    return sum([A[i,j]**2 for i in A.D[0] for j in A.D[1]])



## 2: (Problem 11.8.2) Frobenius_norm_counterexample
#Give a numerical counterxample.
A = listlist2mat([ [1,1,2], [2,1,2], [3,1,1] ])
Q = listlist2mat([ [1,0], [0,1], [0,0] ])



## 3: (Problem 11.8.3) Multiplying a vector by a matrix in terms of the SVD of the matrix
# Use lists instead of Vecs
# Part 1
vT_x_1 = [ 2, 1 ]
Sigma_vT_x_1 = [ 4, 1 ]
U_Sigma_vT_x_1 = [ 1, 4, 0 ]

# Part 2
vT_x_2 = [ 0, 2 ]
Sigma_vT_x_2 = [ 0, 2 ]
U_Sigma_vT_x_2 = [ 2, 0, 0 ]



## 4: (Problem 11.8.4) The SVD of a small simple matrix
# A.D = ({'r1','r2'},{'c1','c2'})
# Row and column labels of SA should be {0,1, ...}
UA = Mat(({0, 1},{0, 1}),{(0,0): 1, (0,1): 0, (1,0): 0, (1,1): 1})
SA = Mat(({0, 1},{0, 1}), {(0,0): 3, (0,1): 0, (1,0): 0, (1,1): 1})
VA = Mat(({0, 1},{0, 1}), {(0,0): 1, (0,1): 0, (1,0): 0, (1,1): -1})


# B.D = ({'r1','r2'},{'c1','c2'})
# Row- and column-labels of SB should be {0,1, ...}
UB = Mat(({0, 1},{0, 1}),{(0,0): 1, (0,1): 0, (1,0): 0, (1,1): 1})
SB = Mat(({0, 1},{0, 1}), {(0,0): 3, (0,1): 0, (1,0): 0, (1,1): 4})
VB = Mat(({0, 1},{0, 1}), {(0,0): 1, (0,1): 0, (1,0): 0, (1,1): 1})


# C.D = ({'r1','r2','r3'},{'c1','c2'})
# Row- and column-labels of SC should be {0,1, ...}
UC = Mat(({0, 1, 2},{0, 1}),{(0,0): 1, (0,1): 0, (1,0): 0, (1,1): 1, (2,0): 0, (2,1): 0})
SC = Mat(({0, 1},{0, 1}), {(0,0): 4, (0,1): 0, (1,0): 0, (1,1): 0})
VC = Mat(({0, 1},{0, 1}), {(0,0): 0, (0,1): 1, (1,0): 1, (1,1): 0})



## 5: (Problem 11.8.5) Closest rank-$k$ matrix
# In both parts, your matrices must use 0, 1, 2, ... , n as the indices.

# Part 1
u = listlist2mat([ [0, -sqrt(0.5)], [sqrt(0.8), 0], [0, -sqrt(0.5)], [sqrt(0.2), 0] ])
s = Mat(({0,1},{0,1}), {(0,0): sqrt(5), (1,1): 2})
vt = listlist2mat([ [0,1,0], [-sqrt(0.5), 0, -sqrt(0.5)] ])
G1 = u*s
H1 = vt

# Part 2
u = listlist2mat([ [sqrt(2)/2, 0], [sqrt(2)/2, 0], [0, 0], [0, -1] ])
s = Mat(({0,1},{0,1}), {(0,0): sqrt(2), (1,1): 1})
vt = listlist2mat([ [0,0,1], [0,-1,0]  ])
G2 = u*s
H2 = vt



## 6: (Problem 11.8.7) Writing SVD_solve
def SVD_solve(U, Sigma, V, b):
    '''
    Input:
      - U: orthogonal matrix
      - Sigma: diagonal matrix with non-negative elements
      - V: orthogonal matrix
      - b: vector
    Output:
      - x: a vector such that U*Sigma*V.tranpose()*x = b
      - 'FAIL': if U*Sigma*V.transpose() has no inverse

    Example:
      >>> U = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): -0.44072022797538285, (1, 2): -0.4580160039142736, (0, 0): -0.15323906505773385, (2, 0): -0.8716906349733183, (1, 0): -0.4654817137547351, (2, 2): 0.08909472804179724, (0, 2): 0.8844679019577585, (2, 1): 0.4818895789856551, (1, 1): -0.7573295942443791})
      >>> Sigma = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 0): 39.37043356298421, (1, 1): 2.2839722460456144, (2, 2): 0.867428292102265})
      >>> V = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0.8797721734901444, (1, 2): -0.7977287698474189, (0, 0): -0.46693900110435005, (2, 0): -0.682398941975231, (1, 0): -0.5624052393414894, (2, 2): 0.5963722979461945, (0, 2): 0.08926865071288784, (2, 1): -0.42269583181462916, (1, 1): -0.21755265229127096})
      >>> b = Vec({0,1,2}, {0:0, 1:1, 2:2})
      >>> x = SVD_solve(U, Sigma, V, b)
      >>> res = b - U*(Sigma*(V.transpose()*x))
      >>> res*res < 1e-20
      True
    '''
    x = V*Sigma*U.transpose()*b
    A = U*Sigma*V.transpose()
    r = A*x - b
    if r*r < 1e-5:
        return x
    return 'FAIL'

'''
prompt for proposed test
>>> V = listlist2mat([ [-1/sqrt(3), 2/sqrt(6), 0], [-1/sqrt(3), -1/sqrt(6), 1/sqrt(2)], [-1/sqrt(3), -1/sqrt(6), -1/sqrt(2)] ])
>>> U = listlist2mat([ [-1/sqrt(3), 1/sqrt(6), 1/sqrt(2)], [-1/sqrt(3), 1/sqrt(6), -1/sqrt(2)], [-1/sqrt(3), -2/sqrt(6), 0] ])
>>> Sigma = listlist2mat([ [2,0,0], [0,1,0], [0,0,1] ])
'''
