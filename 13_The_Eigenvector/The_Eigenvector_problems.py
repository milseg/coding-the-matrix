# version code ccaba3406664+
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec



## 1: (Problem 12.14.1) Finding eigenvalues and -vectors
# Provide eigenvectors as lists.
# If there is only one eigenvalue for a part,
#   use None for one of them

# Part a
p1_part_a_eigenvalue1 = 2
p1_part_a_eigenvector1 = [2,1]
p1_part_a_eigenvalue2 = -1
p1_part_a_eigenvector2 = [1,-1]

# Part b
p1_part_b_eigenvalue1 = 4
p1_part_b_eigenvector1 = [1,3]
p1_part_b_eigenvalue2 = None
p1_part_b_eigenvector2 = None

# Part c
p1_part_c_eigenvalue1 = 6
p1_part_c_eigenvector1 = [1,0]
p1_part_c_eigenvalue2 = 6
p1_part_c_eigenvector2 = [0,1]

# Part d
p1_part_d_eigenvalue1 = 4
p1_part_d_eigenvector1 = [1,1]
p1_part_d_eigenvalue2 = -4
p1_part_d_eigenvector2 = [1,-1]




## 2: (Problem 12.14.2) Finding eigenvectors
# Provide eigenvectors as lists.


# Part a
p2_part_a_lambda1_eigenvector = [1, 1/2]
p2_part_a_lambda2_eigenvector = [1, 1]

# Part b
p2_part_b_lambda1_eigenvector = [0,1,1]
p2_part_b_lambda2_eigenvector = [0,1,-1/3]



## 3: (Problem 12.14.3) Finding the eigenvalue associated with an eigenvector
# Part a
p3_part_a_eigenvalue1 = -1
p3_part_a_eigenvalue2 = 5

# Part b
p3_part_b_eigenvalue1 = 2
p3_part_b_eigenvalue2 = 5



## 4: (Problem 12.14.11) Markov chains and eigenvectors
# a Mat
transition_matrix = ...

# a Vec
definitely_windy_vector = ...

day_after_windy = ...

uniform = ...
day_after_uniform = ...

four_hundred_days_from_now = ...

# Be clever here; no computation is needed:
eigenvalue = ...
eigenvector = ... # as an instance of Vec

