
from vec import Vec, scalar_mul
from mat import Mat

import svd
import matutil

import eigenfaces

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

