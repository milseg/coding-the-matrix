from math import sqrt


#task 10.9.1
def forward_no_normalization(v):
    D = {}
    while len(v) > 1:
        k = len(v)
        # v is a k-element list
        vnew = [(v[2*i]+v[2*i+1])/2 for i in range(k//2)]
        # vnew is a k//2-element list
        w = [(v[2*i]-v[2*i+1]) for i in range(k//2)]
        # w is a list of coefficients
        D.update({(k//2, i): w[i] for i in range(k//2)})
        v = vnew
    D[(0,0)] = v[0]
    return D


#task 10.9.2
def normalize_coefficients(n, D):
    R = {}
    s = 1
    while s <= n//2:
        for i in range(s):
            R[(s,i)] = D[(s,i)]*sqrt(n/(4*s))
        s *= 2
    R[(0,0)] = D[(0,0)]*sqrt(n)
    return R

#task 10.9.3
def forward(v):
    return normalize_coefficients(len(v), forward_no_normalization(v))


#task 10.9.4
def suppress(D, threshold):
    return {k:(0 if abs(v) < threshold else v) for (k,v) in D.items()}

#task 10.9.5
def sparsity(D):
    k = 0
    for i in D:
        if abs(D[i]) > 0:
            k+=1
    return k/len(D)


#task 10.9.6
def unnormalize_coefficients(n, D):
    R = {}
    s = 1
    while s <= n//2:
        for i in range(s):
            R[(s,i)] = D[(s,i)]/sqrt(n/(4*s))
        s *= 2
    R[(0,0)] = D[(0,0)]/sqrt(n)
    return R

#task 10.9.7
def backward_no_normalization(D):
    n = len(D)
    v = [D[(0,0)]]
    s = 2
    while s <= n:
        v = [v[k//2] + D[(s//2, k//2)]*(1 if k%2 == 0 else -1)/2 for k in range(s)]
        s *= 2
    return v


#task 10.9.8
def backward(D):
    return backward_no_normalization(unnormalize_coefficients(len(D), D))


