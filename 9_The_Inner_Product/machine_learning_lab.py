# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from mat import *
from vec import *
from cancer_data import *


#Task 8.4.1
A,b = read_training_data('train.data')
w = Vec(A.D[1], {i: 1 for i in A.D[1]})

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D, {i: (1 if u[i] >= 0 else -1) for i in u.D})

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> fraction_wrong(A, b, w)
        0.3333333333333333
    '''
    err = 0
    v = signum(A*w)
    for i in b.D:
        if v[i] != b[i]:
            err += 1
    #a_d = v*b --> agreements - disagreements
    #len(b.D) --> agreements + disagreements
    #return ((len(b.D) - a_d)/2)/len(b.D) --> disagreements/total
    return err/len(b.D)


print("fraction wrong", fraction_wrong(A, b, w))

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> loss(A, b, w)
        317
    '''
    v = A*w - b
    return v*v


#print("loss ", loss(A,b,w))

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> find_grad(A, b, w) == Vec({'B', 'A'},{'B': -290, 'A': 60})
        True
    '''
    v = 2*(A*w - b)
    v = v*A
    return v

#print("find_grad ", find_grad(A,b,w))

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> sigma = .1
        >>> gradient_descent_step(A, b, w, sigma) == Vec({'B', 'A'},{'B': 27.0, 'A': -5.0})
        True
    '''
    g = find_grad(A,b,w)
    return w - sigma*g

## Ungraded task ##
def gradient_descent(A, b, w, sigma, T):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
        - T: number of iterations to run
    Output: hypothesis vector obtained after T iterations of gradient descent.
    '''
    for i in range(T):
        w = gradient_descent_step(A, b, w, sigma)
        if (i+1)%30 == 0:
            print("loss_function", loss(A,b,w))
            print("fraction_wrong", fraction_wrong(A,b,w))
    return w

r = gradient_descent(A,b,w,1e-9,500)
print("corrected vector", r)
print("    ")
print("zero vector")
r = gradient_descent(A,b,Vec(A.D[1], {}), 1e-9, 200)

print("corrected vector", r)


print(" ")
print("applying to real data")


A,b = read_training_data('validate.data')

print("fraction wrong ", fraction_wrong(A,b,r))
print("loss ", loss(A,b,r))
