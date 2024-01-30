

#1 - Solve for an arbitraly n row - subset of matrix A
A_square = Mat((R_square, A.D[1]), {(r,c):A[r,c] for r,c in A.f if r in R_square})
b_square = Vec(R_square, {k:b[k] for k in R_square})
x = solve(A_square, b_square)
#for a coincidence x could be a vertex. we chould check it at this point and we would be done

#2 - add m-n variables to matrix A with  m-n non-negative constraints. Also adds new variable to the complementary (R-R_square) contraints in order to make it satisfy the constraint 
A_x = A*x
missing = A.D[0].difference(R_square) # set of row-labels not in R_square
extra = {new_name(r) for r in missing}
f = dict_union(A.f,
{(r,new_name(r)):1 for r in missing},
{(e, e):1 for e in extra})
A_with_extra = Mat((A.D[0].union(extra), A.D[1].union(extra)), f)
b_with_extra = Vec(b.D.union(extra), b.f) # use sparsity convention

#3 - R_square inclusions for the new augmented system
# if constraint r is not satisfied by x then include r in R_square. We can now satisfy the constraint with the new variable
# and
# if constraint r is satisfied by x then include new_name(r) in R - includes the non-negative contraint keeping consistency with the original constraint
new_R_square = R_square | {r if A_x[r]-b[r] < 0 else new_name(r) for r in missing}
#now we have a vertex for the augmented system


#4 - Setup augmented system goal aiming to zeroing the new variables and apply simplex
c = Vec(A.D[1].union(extra), {e:1 for e in extra})
answer= optimize(A_with_extra, b_with_extra, c, new_R_square)

#5 - If simplex finds object value 0 then we got a vertex for the original LP, else the original LP must have no solutions
#catching vertex labels:
basis_candidates=list(new_R_square | D[0])
R_square.clear()
R_square.update(set(basis_candidates[:n]))
