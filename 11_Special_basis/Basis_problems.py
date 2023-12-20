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


#task 10.9.9
def dictlist_helper(dlist, k):
    return [d[k] for d in dlist]

#we apply wavelets coordinates first in the rows and then in the columns
def forward2d(vlist):
    v1 = [forward(el) for el in vlist]
    return {i:forward(dictlist_helper(v1, i)) for i in v1[0]}

def suppress2d(D_dict, threshold):
    return {k1:{k:(v if abs(v) > threshold else 0) for k,v in v1.items()} for k1,v1 in D_dict.items()}

def sparsity2d(D_dict):
    for i in D_dict:
        l += len(D_dict[i])
        for j in D_dict[i]:
            if D_dict[i][j] > 0:
                k+=1
    return k/l

def listdict2dict(L_dict, i):
    return {k:v[i] for k,v in L_dict.items()}

def listdict2dictlist(listdict):
    return [{k:listdict[k][i] for k in listdict} for i in range(len(listdict[(0,0)]))]


def backward2d(D):
    l1 = listdict2dictlist({k:backward(D[k]) for k in D})
    return [backward(v) for v in l1]

def image_round(img):
    return [[min(abs(round(img[i][j])), 255) for j in range(len(img[i]))] for i in range len(img)]


