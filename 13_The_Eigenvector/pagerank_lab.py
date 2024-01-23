# version code 53ead35ddb8a+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from mat import Mat
from math import sqrt
import pagerank



## 1: (Task 12.12.1) Find Number of Links
def find_num_links(L):
    '''
    Input:
        - L: a square matrix representing link structure
    Output:
        - A vector mapping each column label of L to
          the number of non-zero entries in the corresponding
          column of L
    Example:
        >>> from matutil import listlist2mat
        >>> find_num_links(listlist2mat([[1,1,1],[1,1,0],[1,0,0]]))
        Vec({0, 1, 2},{0: 3, 1: 2, 2: 1})
    '''
    ones_vec = Vec(L.D[0], {i:1 for i in L.D[0]})
    return ones_vec*L



## 2: (Task 12.12.2) Make Markov
def make_Markov(L):
    '''
    Input:
        - L: a square matrix representing link structure
    Output:
        - None: changes L so that it plays the role of A_1
    Example:
        >>> from matutil import listlist2mat
        >>> M = listlist2mat([[1,1,1],[1,0,0],[1,0,1]])
        >>> make_Markov(M)
        >>> M
        Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 1.0, (2, 0): 0.3333333333333333, (0, 0): 0.3333333333333333, (2, 2): 0.5, (1, 0): 0.3333333333333333, (0, 2): 0.5})
    '''
    nls = find_num_links(L)
    for i,j in L.f:
        if nls[j] == 0 and i == j:
            L[i,j] = 1
            continue
        elif nls[j] > 0:
            L[i,j] = L[i,j]/nls[j]
        else:
            L[i,j] = 0



## 3: (Task 12.12.3) Power Method
def power_method(A1, i):
    '''
    Input:
        - A1: a matrix
        - i: number of iterations to perform
    Output:
        - An approximation to the stationary distribution
    Example:
        >>> from matutil import listlist2mat
        >>> power_method(listlist2mat([[0.6,0.5],[0.4,0.5]]), 10)
        Vec({0, 1},{0: 0.5464480874307794, 1: 0.45355191256922034})
    '''
    l = len(A1.D[0])
    for r,j in A1.f:
        A1[r,j] = 0.85*A1[r,j] + 0.15*1/l
    v = Vec(A1.D[1], {r: 1/l for r in A1.D[1]})
    for r in range(i):
        on = v*v
        v = A1*v
        nn = v*v
        print("norm ratio ", nn/on, " iteration ", r+1)
    return v



## 4: (Task 12.12.4) Jordan
#pagerank.find_word('jordan')
number_of_docs_with_jordan = 10159



## 5: (Task 12.12.5) Wikigoogle
def wikigoogle(w, k, p):
    '''
    Input:
        - w: a word
        - k: number of results
        - p: pagerank eigenvector
    Output:
        - the list of the names of the kth heighest-pagerank Wikipedia
          articles containing the word w
    '''
    related = pagerank.find_word(w)
    related.sort(key=lambda x:p[x], reverse=True)
    return related[:k]

## 6: (Task 12.12.6) Using Power Method
links = pagerank.read_data()
make_Markov(links)
p = power_method(links, 10)
#wikigoogle('jordan', 5, p)
results_for_jordan = ['2007', '2006', '2005', 'paris', 'israel']# give 5 of them as a list
results_for_obama  = ['united states', 'president of the united states', 'chicago', 'democratic party (united states)', 'illinois']
results_for_tiger  = ['france', 'england', '2006', 'india', 'sweden']
results_for_matrix = ['1999', 'religion', 'internet', '1965', 'sydney']




## 7: (Task 12.12.7) Power Method Biased
def power_method_biased(A1, i, r):
    '''
    Input:
        - A1: a matrix, as in power_method
        - i: number of iterations
        - r: bias label
    Output:
        - Approximate eigenvector of .55A_1 + 0.15A_2 + 0.3A_r
    '''
    l = len(A1.D[0])
    for rl,j in A1.f:
        bias = 0.3 if j == r else 0
        A1[rl,j] = 0.55*A1[rl,j] + 0.15*1/l + bias
    v = Vec(A1.D[1], {rl: 1/l for rl in A1.D[1]})
    for rl in range(i):
        on = v*v
        v = A1*v
        nn = v*v
        print("norm ratio ", nn/on, " iteration ", rl+1)
    return v


links = pagerank.read_data()
make_Markov(links)
p_sport = power_method_biased(links, 10, "sport")
sporty_results_for_jordan = ['2007', '2006', '2005', 'basketball', 'paris']
sporty_results_for_obama  = ['united states', 'president of the united states', 'chicago', 'democratic party (united states)', 'illinois']
sporty_results_for_tiger  = ['france', 'england', '2006', 'india', 'ireland']
sporty_results_for_matrix = ['1999', 'internet', 'religion', 'sydney', '1965']

