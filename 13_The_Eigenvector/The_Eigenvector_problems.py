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
transition_matrix = Mat(({'S','R','F','W'}, {'S','R','F','W'}), {('S','S'): 0.5, ('S', 'R'): 0.2, ('S', 'W'): 0.1, ('R', 'S'): 0.2, ('R', 'R'): 0.6, ('F', 'R'): 0.2, ('F', 'F'): 0.4, ('F', 'W'): 0.8, ('W', 'S'): 0.3, ('W', 'F'): 0.6, ('W', 'W'): 0.1})

# a Vec
definitely_windy_vector = Vec({'S', 'R', 'F', 'W'}, {'W': 1.0})

day_after_windy = Vec({'R', 'F', 'W', 'S'},{'S': 0.1, 'R': 0.0, 'F': 0.8, 'W': 0.1})

uniform = Vec({'S', 'R', 'F', 'W'}, {'S': 0.25, 'R': 0.25, 'F': 0.25, 'W': 0.25})

day_after_uniform = Vec({'R', 'F', 'W', 'S'},{'S': 0.19999999999999998, 'R': 0.2, 'F': 0.35000000000000003, 'W': 0.24999999999999997})

four_hundred_days_from_now = Vec({'R', 'F', 'W', 'S'},{'S': 0.0909090909090911, 'R': 0.04545454545454557, 'F': 0.5000000000000009, 'W': 0.3636363636363643})

# Be clever here; no computation is needed:
eigenvalue = 1.0
eigenvector = four_hundred_days_from_now # as an instance of Vec

