import numpy as np
from matrix import Matrix

np.random.seed(0)

a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

print(a)
print(b)

with open('artifacts/matrix+.txt', 'w') as f:
    print(a + b, file=f)

with open('artifacts/matrix*.txt', 'w') as f:
    print(a * b, file=f)

with open('artifacts/matrix@.txt', 'w') as f:
    print(a @ b, file=f)
