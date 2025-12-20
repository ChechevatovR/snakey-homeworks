import sys

import numpy as np

class Matrix:
    _matmul_cache = dict()

    def __init__(self, data: np.ndarray):
        if data.ndim != 2:
            raise ValueError("Array for matrix must be 2-dimensional")
        self.data = data

    def width(self):
        return self.data.shape[1]

    def height(self):
        return self.data.shape[0]

    """
    This implementation uses trace of the matrix as hash
    
    tr A = sum A[i][i] 
    """
    def __hash__(self):
        return int(sum([self.data[i][i] for i in range(min(self.height(), self.width()))]))

    def __str__(self):
        return self.data.__str__()

    def __add__(self, other):
        if self.height() != other.height() or self.width() != other.width():
            raise ValueError("Matrix shape mismatch for addition")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.height() != other.height() or self.width() != other.width():
            raise ValueError("Matrix shape mismatch for element-wise multiplication")
        return Matrix(self.data * other.data)

    def matmul(self, other):
        return Matrix(self.data @ other.data)

    def __matmul__(self, other):
        if self.width() != other.height():
            raise ValueError("Matrix shape mismatch for matrix multiplication")

        matmul_cache_key = (hash(self), hash(other))
        if matmul_cache_key not in self._matmul_cache:
            print(f'Computing matmul, {matmul_cache_key=}', file=sys.stderr)
            result = self.matmul(other)
            Matrix._matmul_cache[matmul_cache_key] = result
            return result
        print(f'Matmul cache hit, {matmul_cache_key=}', file=sys.stderr)
        return Matrix._matmul_cache[matmul_cache_key]

