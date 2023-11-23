# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one



## 1: (Problem 7.9.2) Recognizing Echelon Form
# Write each matrix as a list of row lists

echelon_form_1 = [[   1,2,0,2,0 ],
                  [   0,1,0,3,4 ],
                  [   0,0,2,3,4 ],
                  [   0,0,0,2,0 ],
                  [   0,0,0,0,4 ]]

echelon_form_2 = [[   0,4,3,4,4   ],
                  [   0,0,4,2,0 ],
                  [   0,0,0,0,1 ],
                  [   0,0,0,0,0 ]]

echelon_form_3 = [[   1,0,0,1 ],
                  [   0,0,0,1 ],
                  [   0,0,0,0 ]]

echelon_form_4 = [[   1,0,0,0 ],
                  [   0,1,0,0 ],
                  [   0,0,0,0 ],
                  [   0,0,0,0   ]]



## 2: (Problem 7.9.3) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> is_echelon([[1,1]])
        True
        >>> is_echelon([[1]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
    '''
    mincol = -1
    for r in A:
        for i in range(len(r)):
            if r[i] != 0:
                if i <= mincol:
                    return False
                break
        mincol = i
    return True



## 3: (Problem 7.9.4) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = [1,3]
echelon_form_vec_b = [-3,-2,3]
echelon_form_vec_c = [-5, 2, 2]



## 4: (Problem 7.9.5) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,2]



## 5: (Problem 7.9.6) Echelon Solver
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    '''
    maxcol = len(label_list)
    newmaxcol = maxcol
    D = label_list
    v = Vec(set(D), {})
    for i in reversed(range(len(rowlist))):
        for j in reversed(range(maxcol)):
            if rowlist[i][D[j]] != 0: # or > 1e14 to account for float point errors
                newmaxcol = j
        if newmaxcol < maxcol:
            v[D[newmaxcol]] = (b[i] - rowlist[i]*v)/rowlist[i][D[newmaxcol]]
            maxcol = newmaxcol
    return v



## 6: (Problem 7.9.7) Solving General Matrices via Echelon
rowlist = [ Vec({'A', 'D', 'B', 'C'},{'A': one, 'D': one, 'B': one, 'C': 0}),
            Vec({'A', 'D', 'B', 'C'},{'A': 0, 'D': 0, 'B': one, 'C': 0}),
            Vec({'A', 'D', 'B', 'C'},{'A': 0, 'D': 0, 'B': 0, 'C': one}),
            Vec({'A', 'D', 'B', 'C'},{'A': 0, 'D': one, 'B': 0, 'C': 0}) ]    # Provide as a list of Vec instances
label_list = [ 'A', 'B', 'C', 'D'] # Provide as a list
b = [ 1,1,0,0 ]          # Provide as a list of GF(2) values



## 7: (Problem 7.9.8) Nullspace A
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## 8: (Problem 7.9.9) Nullspace B
null_space_rows_b = {4} # Put the row numbers of M from the PDF

