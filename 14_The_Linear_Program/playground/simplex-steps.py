


#simplex steps
#1 - Extract the subsystem
R_square = #subsystem label rows
A_square = Mat((R_square, A.D[1]), {(r,c):A[r,c] for r,c in A.f if r in R_square})
b_square = Vec(R_square, {k:b[k] for k in R_square})


#2 - Find subsystem vertex
x = solve(A_square, b_square)

#3 - Find feasible solution to dual LP
y_square = solve(A_square.transpose(), c)
y = Vec(R, y_square.f)


#4 - termination condition
if min(y.values()) >= 0: return ('OPTIMUM', x) #found optimum!


#5 - choose which label is going to exit 
R_leave = {i for i in R if y[i] < 0} #labels at which y is negative
r_leave = min(R_leave, key=hash) #choose first label where y is negative

#6 - find a vector w that is mathematicaly good to move
d = Vec(R_square, {r_leave:1})
w = solve(A_square, d)

#7 - groups new candidates for entering A_square matrix
Aw = A*w # compute once because we use it many times
R_enter = {r for r in R if Aw[r] < 0}

#8 - if r_enter is empty, objective value is unbounded
if len(R_enter)==0: return ('UNBOUNDED', None)

#9 - choose which row enters based on minimum delta value
Ax = A*x # compute once because we use it many times
delta_dict = {r:(b[r] - Ax[r])/(Aw[r]) for r in R_enter}
delta = min(delta_dict.values())
r_enter = min({r for r in R_enter if delta_dict[r] == delta}, key=hash)[0]

#10 - finally exchanges rows and start again
R_square.discard(r_leave)
R_square.add(r_enter)


