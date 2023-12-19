>>> from read_data import read_vectors
>>> read_vectors('age-height.txt')
[Vec({'height', 'age'},{'age': 18.0, 'height': 76.1}), Vec({'height', 'age'},{'age': 19.0, 'height': 77.0}), Vec({'height', 'age'},{'age': 20.0, 'height': 78.1}), Vec({'height', 'age'},{'age': 21.0, 'height': 78.2}), Vec({'height', 'age'},{'age': 22.0, 'height': 78.8}), Vec({'height', 'age'},{'age': 23.0, 'height': 79.7}), Vec({'height', 'age'},{'age': 24.0, 'height': 79.9}), Vec({'height', 'age'},{'age': 25.0, 'height': 81.1}), Vec({'height', 'age'},{'age': 26.0, 'height': 81.2}), Vec({'height', 'age'},{'age': 27.0, 'height': 81.8}), Vec({'height', 'age'},{'age': 28.0, 'height': 82.8}), Vec({'height', 'age'},{'age': 29.0, 'height': 83.5})]
>>> a = []
>>> vs = read_vectors('age-height.txt')
>>> b = []
>>> for v in vs:
...  vs.append(list2vec([v['age'], 1]))
...  b.append(v['height'])
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\vec.py", line 21, in getitem
    assert k in v.D
AssertionError
>>> for v in vs:
...  print(v)
...

 age height
-----------
  18   76.1

 age height
-----------
  19     77

 age height
-----------
  20   78.1

 age height
-----------
  21   78.2

 age height
-----------
  22   78.8

 age height
-----------
  23   79.7

 age height
-----------
  24   79.9

 age height
-----------
  25   81.1

 age height
-----------
  26   81.2

 age height
-----------
  27   81.8

 age height
-----------
  28   82.8

 age height
-----------
  29   83.5

  0 1
-----
 18 1

  0 1
-----
 19 1

  0 1
-----
 20 1

  0 1
-----
 21 1

  0 1
-----
 22 1

  0 1
-----
 23 1

  0 1
-----
 24 1

  0 1
-----
 25 1

  0 1
-----
 26 1

  0 1
-----
 27 1

  0 1
-----
 28 1

  0 1
-----
 29 1
>>> for v in vs:
...  if 'age' in v.D and 'height' in v.D:
...   vs.append(list2vec([v['age'], 1]))
...   b.append(v['height'])
...
>>> b = list2vec(b)
>>> QR_solve(mat2rowdict(vs), b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 44, in mat2rowdict
    return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}
AttributeError: 'list' object has no attribute 'D'
>>> QR_solve(rowdict2mat(vs), b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 99, in rowdict2mat
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 99, in <dictcomp>
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\vec.py", line 21, in getitem
    assert k in v.D
AssertionError
>>> rowdict2mat(vs)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 99, in rowdict2mat
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 99, in <dictcomp>
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\vec.py", line 21, in getitem
    assert k in v.D
AssertionError
>>> vs = []
>>> b = []
>>> for v in vs:
...  if 'age' in v.D and 'height' in v.D:
...   vs.append(list2vec([v['age'], 1]))
...   b.append(v['height'])
...
>>> rowdict2mat(vs)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 98, in rowdict2mat
    col_labels = value(rowdict).D
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 32, in value
    return next(iter(d.values())) if isinstance(d, dict) else d[0]
IndexError: list index out of range
>>> rowdict2mat({i: vs[ivs)
  File "<stdin>", line 1
    rowdict2mat({i: vs[ivs)
                          ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> rowdict2mat({i: vs[i] for i in range(len(vs))})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 98, in rowdict2mat
    col_labels = value(rowdict).D
  File "C:\Users\Milton\Documents\Projetos\2023\Math\Applied Math\CodingTheMatrix\Lab\matrix\10_Orthogonalization\matutil.py", line 32, in value
    return next(iter(d.values())) if isinstance(d, dict) else d[0]
StopIteration
>>> vs[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> vs = read_data('age-height.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'read_data' is not defined
>>> vs = read_vectors('age-height.txt')
>>> l = []
>>> b = []
>>> for v in vs:
...  if 'age' in v.D and 'height' in v.D:
...   vs.append(list2vec([v['age'], 1]))
...   l.append(list2vec([v['age'], 1])))
  File "<stdin>", line 4
    l.append(list2vec([v['age'], 1])))
                                     ^
SyntaxError: unmatched ')'
>>> for v in vs:
...  if 'age' in v.D and 'height' in v.D:
...   l.append(list2vec([v['age'], 1]))
...   b.append(v['height'])
...
>>> rowdict2mat(l)
Mat(({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, {0, 1}), {(0, 0): 18.0, (0, 1): 1, (1, 0): 19.0, (1, 1): 1, (2, 0): 20.0, (2, 1): 1, (3, 0): 21.0, (3, 1): 1, (4, 0): 22.0, (4, 1): 1, (5, 0): 23.0, (5, 1): 1, (6, 0): 24.0, (6, 1): 1, (7, 0): 25.0, (7, 1): 1, (8, 0): 26.0, (8, 1): 1, (9, 0): 27.0, (9, 1): 1, (10, 0): 28.0, (10, 1): 1, (11, 0): 29.0, (11, 1): 1})
>>> QR_solve(rowdict2mat(l), list2vec(b))
Vec({0, 1},{1: 64.92832167832181, 0: 0.6349650349650294})
>>> y
