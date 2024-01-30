from cancer_data import read_training_data
from vec import Vec
from matutil import mat2rowdict

print("reading training data")
feat_cols = {'area(worst)','smoothness(worst)', 'texture(mean)'}
A,b = read_training_data('train.data', feat_cols) 
print("training data read")

for x in b.D:
    print("b first element ", x)
    break

#bypass tasks 13.13.1 to 13.13.5

nonNegCons = {-x for x in b.D}
A.D[0] = A.D[0].union(nonNegCons)
A.D[1] = A.D[1].union(b.D).union('gamma')


def multiply_matrix_row(A, i, s):
    for j in A.D[1]:
        A[i,j] = A[i,j]*s


for i in b.D:
    if b[i] == 1:
        A[i, 'gamma'] = -1
    else: #b[i] == -1
        multiply_matrix_row(A, i, -1)
        A[i, 'gamma'] = 1
    A[i,i] = 1
    A[-i,i] = 1
    b[i] = 1



c = Vec(A.D[1], {i: 1 for i in b.D})
R_square = b.D
rem = len(A.D[1])-len(R_square)
for x in nonNegCons:
    R_square = R_square.add(x)
    rem = rem - 1
    if rem == 0:
        break

b.D = b.D.union(nonNegCons)

#find vertex
if not find_vertex(A, b, R_square):
    print("couldnt find a vertex")
    exit()

print("vertex found")

sol = optimize(A, b, c, R_square)


#Task 13.13.6
w = Vec(feat_cols, {f:sol[f] for f in feat_cols})
gamma = sol['gamma']


def C(feature_vector):
    global w, gamma
    return 1 if w*feature_vector > gamma else -1


def test_data(path):
    A,b = read_training_data(path, feat_cols)
    errors = 0
    feats = mat2rowdict(A)
    sz = len(feats)
    print("reading ", sz, " records")
    for i in feats:
        if c(feats[i]) != b[i]:
            errors += 1
    print("errors ", errors, " (", (errors/sz)*100, "%)")


#Task 13.13.7 - Training data test
def test_training_data(path):
    test_data('train.data')

#Task 13.13.8 - Validation data test
def test_validation_data(path):
    test_data('validate.data')


