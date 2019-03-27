import numpy as np

def HighOrderApprox(x, y, order):
  l = len(x)
  if (order >= l):
    order = l - 1
  
  A = order_array = np.ones([l, 1])
  B = np.array([y]).T
  xx = np.array([x]).T
  for i in range(order):
    order_array = order_array*xx
    A = np.concatenate((A, order_array), axis=1)
  
  A_T = A.T;
  a = np.linalg.inv(A_T.dot(A)).dot(A_T).dot(B)
  
  return a
