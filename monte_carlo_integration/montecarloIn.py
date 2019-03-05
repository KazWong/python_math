import math
import random
import matplotlib.pyplot as plt

def In_Pi(throws):
  _sysrand = random.SystemRandom()
  area = 0

  for i in xrange(throws):
    randX = _sysrand.uniform(0, 1)
    randY = _sysrand.uniform(0, 1)
    
    randA = (randX*randX) + (randY*randY)
    if (1. >= randA):
      area = area + 1

  pi = 4 * (float(area)/float(throws))

  return pi

 

if __name__ == '__main__':
  lpi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
  pi = []
  x = []
  mpi = []
  rel_err = []
  _rel_err = []
  j = 0
  for i in xrange(1, 100000, 2):
    pi.append(In_Pi(i))
    x.append(i)
    mpi.append(lpi)
    rel_err.append(math.fabs((pi[j] - mpi[j]) / mpi[j]))
    _rel_err.append(1 / math.sqrt(i))
    j += 1
    
  plt.subplot(211)
  plt.xscale("log")
  plt.xlabel('# of Sample')
  plt.ylabel('Value')
  plt.plot(x, pi, x, mpi)
  
  plt.subplot(212)
  plt.xscale("log")
  plt.yscale("log")
  plt.xlabel('# of Sample')
  plt.ylabel('Relative Error')
  plt.plot(x, rel_err, x, _rel_err, 'r--')
  
  plt.show()
