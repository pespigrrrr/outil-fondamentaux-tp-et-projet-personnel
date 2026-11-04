import numpy as np


def transposee(A):
  n = len(A)
  p = len(A[0])
  return [[A[i][j] for i in range(n)] for j in range(p)]


def produit(A, B):
    n, p = len(A), len(A[0])
    if len(B) != p:
        raise ValueError("dimensions incompatibles")
    q = len(B[0])
    C = [[0] * q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            somme = 0
            for k in range(p):
                somme = somme + A[i][k] * B[k][j]
            C[i][j] = somme
    return C

identite = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]

print(produit(A, identite) == A)

print(produit([[1, 2], [3, 4]], [[0, 1], [1, 0]]))

A = np.array([[1.0, 2.0, 2.0],
              [1.0, 3.0, -2.0],
              [3.0, 5.0, 8.0]])

b = np.array([2.0, -1.0, 8.0])

print(A.shape)
print(A.T)         
print(A @ A)        
print(A * A)