import numpy as np
from matrix import Matrix

# Матрицы с одинаковым хешом нашел аналитически
a = Matrix(np.array([[1, 0], [0, 0]]))
b = d = Matrix(np.array([[10, 10], [10, 10]]))
c = Matrix(np.array([[0, 0], [0, 1]]))

print(a)
print(c)
print(hash(a), hash(c))
print(b)

with(open('artifacts/A.txt', 'w')) as f:
    print(a, file=f)
with(open('artifacts/B.txt', 'w')) as f:
    print(b, file=f)
with(open('artifacts/C.txt', 'w')) as f:
    print(c, file=f)
with(open('artifacts/D.txt', 'w')) as f:
    print(d, file=f)
with(open('artifacts/AB.txt', 'w')) as f:
    print(a @ b, file=f)
with(open('artifacts/CD.txt', 'w')) as f:
    print(c.matmul(d), file=f)
with(open('artifacts/hash.txt', 'w')) as f:
    print(hash(a @ b), hash(c.matmul(d)), sep='\n', file=f)
