
def orthogonal_vec2rep(Q,b):
    return Q*b


def orthogonal_change_of_basis(A, B, a):
    return B*(a*A)

def orthonormal_projection_orthogonal(W, b):
    return b - (W*b)*W
