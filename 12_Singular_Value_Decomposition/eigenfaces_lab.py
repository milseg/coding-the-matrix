# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec, scalar_mul
from mat import Mat

import svd
import matutil

import eigenfaces
from image_mat_util import image2display 


## Task 1
vecD = { (d1, d2) for d1 in range(189) for d2 in range(166) }
# see documentation of eigenfaces.load_images

fcs = eigenfaces.load_images('faces').items() 
face_images = {ind: Vec(vecD, {(i,j): fl[i][j] for i in range(189) for j in range(166)}) for ind,fl in fcs} # dict of Vecs

## Task 2

centroid = scalar_mul(sum(face_images.values()), 1/len(face_images))
centered_face_images = { ind: v - centroid for ind,v in face_images.items() }

## Task 3

A = matutil.rowdict2mat(centered_face_images) # centered image vectors
V = svd.factor(A)[2]

orthonormal_basis = Mat(({d for d in range(10)}, A.D[1]),  {(i,j): V[j,i] for i in range(10) for j in A.D[1]}) # 10 rows

## Task 4

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def projected_representation(M, x):
    '''
    Input:
        - M: a matrix with orthonormal rows with M.D[1] == x.D
        - x: a vector
    Output:
        - the projection of x onto the row-space of M
    Examples:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> projected_representation(M, x)
        Vec({0, 1},{0: 1, 1: 2})
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> projected_representation(M, x)
        Vec({0, 1},{0: 1.6, 1: 2.333333333333333})
    '''
    return M*x

## Task 5

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def projection_length_squared(M, x):
    '''
    Input:
        - M: matrix with orthonormal rows with M.D[1] == x.D
        - x: vector
    Output:
        - the square of the norm of the projection of x into the
          row-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> projection_length_squared(M, x)
        5
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> projection_length_squared(M, x)
        5.644424691358024
    '''
    pr = projected_representation(M, x)
    return pr*pr

## Task 6

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def distance_squared(M, x):
    '''
    Input:
        - M: matrix with orthonormal rows with M.D[1] == x.D
        - x: vector
    Output:
        - the square of the distance from x to the row-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> distance_squared(M, x)
        9
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> distance_squared(M, x)
        8.355575308641976
    '''
    return x*x - projection_length_squared(M, x)

## Task 7

distances_to_subspace = [distance_squared(orthonormal_basis, x) for x in centered_face_images.values()]
maxd = max(distances_to_subspace)
mind = min(distances_to_subspace)
## Task 8
nfcs = eigenfaces.load_images('unclassified', 11).items() 
uncl_images = {ind: Vec(vecD, {(i,j): fl[i][j] for i in range(189) for j in range(166)}) - centroid for ind,fl in nfcs} 

def in_range(M, v, mn, mx):
    d = distance_squared(M, v)
    return d >= mn and d <= mx

classified_as_faces = {ind for ind,v in uncl_images.items() if in_range(orthonormal_basis, v, mind, maxd)}# of dictionary keys

## Task 9

threshold_value = 38634036.00224697#the greatest face distance

## Task 10

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def project(M, x):
    '''
    Input:
        - M: an orthogonal matrix with row-space equal to x's domain
        - x: a Vec
    Output:
        - the projection of x into the column-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0], [0, 1], [0, 0]])
        >>> project(M, x)
        Vec({0, 1, 2},{0: 1, 1: 2, 2: 0})
        >>> M = listlist2mat([[3/5, 0], [1/5, 2/3], [1/5, 1/3]])
        >>> project(M, x)
        Vec({0, 1, 2},{0: 0.96, 1: 1.8755555555555554, 2: 1.0977777777777777})
    '''
    return projected_representation(M, x)*M

def vec2img(v, basis, centroid):
    ig = project(basis, v)+centroid
    return [[ig[i,j] for j in range(166)] for i in range(189)]

## Task 11

# see documentation for image.image2display
ig = vec2img(uncl_images[4], orthonormal_basis, centroid)
image2display(ig)

## Task 12

ig = vec2img(uncl_images[6], orthonormal_basis, centroid)
image2display(ig)

ig = vec2img(uncl_images[8], orthonormal_basis, centroid)
image2display(ig)
