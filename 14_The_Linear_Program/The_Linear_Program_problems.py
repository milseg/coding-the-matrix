from solver import solve
from mat import Mat
from vec import Vec
from matutil import listlist2mat
from vecutil import list2vec
from simplex import optimize, find_vertex

#13.16.2
def find_move_helper(A, r):
    return solve(A, Vec(A.D[0], {r:1}))


#13.16.3
def find_move_direction(A, x, r):
    return find_move_helper(A, r)


#13.16.4
def find_move(A, x, r):
    lb = float('inf')
    w = find_move_direction(A, x, r)
    for i in A.D[0]:
        if w[i] < 0:
            lb = min(lb, abs(x[i]/w[i]))
    return (w,lb)


r = find_move_helper(listlist2mat([ [1, 1, 0], [0, 1, 1], [1, 0, 1] ]), 2)
print(r)


(r,lb) = find_move(listlist2mat([ [1, 1, 0], [0, 1, 1], [1, 0, 1] ]), list2vec([2,4,6]), 2)
print(r)
print("lambda", lb)

#13.16.5
'''
xi: Number of chocolates of type i
profit = x1 + 1.6*x2
constraints:
(peanuts) 50*x1 <= 200
(chocolate) 100*x1 + 150*x2 <= 1000
(caramel) 50*x2 <= 300
(sugar) 50*x1 + 30*x2 <= 300
'''
A = listlist2mat([ [-50, 0], [-100, -150], [0, -50], [-50, -30], [1, 0], [0, 1] ])
b = list2vec([-200,-1000,-300,-300,0,0])
c = list2vec([-1, -1.6])
R_square = {4,5}
r = optimize(A, b, c, R_square)
print("simplex chocolate solution", r)#1 n&n and 2 venus

#13.16.6
'''
xi: Number of visits to city i
profit = 35*xa + 50*xb + 55*xc
(kids city b) xb <= 3
(expenses) 20*xa + 30*xb + 35*xc <= 195
'''
A = listlist2mat([ [0, -1, 0], [-20, -30, -35], [1,0,0], [0,1,0], [0,0,1] ])
b = list2vec([-3, -195, 0, 0, 0])
c = list2vec([-35, -50, -55])
R_square = {0,1,2}
if not find_vertex(A, b, R_square):
    print("vertex not found")
    exit()

r = optimize(A, b, c, R_square)
print("simplex ice-cream van solution", r)
