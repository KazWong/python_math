import numpy as np

def HighOrderApprox(x, y, order):
  l = len(x)
  if (not l > order):
    order = l - 1
  
  A = np.ones([l, 1])
  B = y.reshape([-1, 1])
  order_array = xx = x.reshape([-1, 1])
  for i in range(order):
    A = np.concatenate((A, order_array), axis=1)
    order_array = order_array*xx
  
  A_t = A.transpose();
  a = np.linalg.inv(A_t.dot(A)).dot(A_t).dot(B)
  
  return a
