'''
  cpp RIP
/**
 * main.cpp
 *  area of two overlapping rectangles
 *  Created on: 6 Nov 2016
 *      Author: Kaz
**/
'''

import math
import numpy as np
import random
import matplotlib.pyplot as plt


def M(K, L, M, N, P, Q, R, S):
  SA = (M - K) * (N - L)
  SB = (R - P) * (S - Q)
  SI = max(0, min(M, R) - max(K, P)) * max(0, min(N, S) - max(L, Q))
  return SA+SB-SI


if __name__ == '__main__':
  area = M(1, 1, 2, 2, 3, 3, 4, 4)
  print("MN : 1, 1, 2, 2\t\tAB : 3, 3, 4, 4 =", area) #2

  area = M(1, 1, 3, 3, 1, 1, 3, 3)
  print("MN : 1, 1, 3, 3\t\tAB : 1, 1, 3, 3 =", area) #4

  area = M(1, 1, 2, 2, 1, 1, 3, 3)
  print("MN : 1, 1, 2, 2\t\tAB : 1, 1, 3, 3 =", area) #4

  area = M(5, 5, 6, 6, 1, 1, 7, 7)
  print("MN : 5, 5, 6, 6\t\tAB : 1, 1, 7, 7 =", area) #36

  area = M(1, 1, 2, 10, 1, 1, 10, 2)
  print("MN : 1, 1, 2, 10\tAB : 1, 1, 10, 2 =", area) #17

  area = M(-4, 1, 2, 6, 0, -1, 4, 3)
  print("MN : -4, 1, 2, 6\tAB : 0, -1, 4, 3 =", area) #42


