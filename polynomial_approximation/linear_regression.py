import numpy as np

def LeastSquare(x, y):
  l = len(x)
  cov_m = np.cov(x, y, bias=1)
  a = cov_m[0][1] * l
  b = cov_m[0][0] * l

  m = a / b
  c = np.mean(y) - m * np.mean(x)
  
  return m, c

def PseudoInverse(x, y):
  A = np.concatenate((np.ones([len(x), 1]), x.reshape([-1, 1])), axis=1)
  B = y.reshape([-1, 1])

  A_t = A.transpose();
  A = np.linalg.inv(A_t.dot(A)).dot(A_t)
  a = A.dot(B)
  
  return a[1], a[0]
