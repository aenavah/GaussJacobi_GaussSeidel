import numpy as np
import pandas as pd

def norm(matrix):
  f = np.sqrt(np.sum(matrix**2))
  return f


def GaussJacobi(A, b, D, tol = 10**(-5), N = 10000):
  '''Takes in required inputs A and b, and optional inputs N and tol'''
  '''solves Ax=b with initial guess x0, and max number of iterations N'''
  errors = []
  n = len(b)
  x0 = np.zeros(n)
  x = np.copy(x0)
  for k in range(0, N):
    for i in range(n):
      summ = 0.0
      for j in range(0, n):
        if j != i:
          summ += A[i,j]*x0[j]
      if abs(A[i,i]) <= 10**-16:
        return x, k, 0, 0
      x[i] = (-summ + b[i])/A[i, i]
    error = (norm(x- x0))/(norm(x))
    if error < tol:
      df = pd.DataFrame(errors)
      df.to_csv("Errors_GaussJacobi_D=" + str(D) + ".csv")
      return x, k, 1, df
    errors.append([k, error])
    x0 = np.copy(x)
  return x, k, 0, 0

def GaussSeidel(A, b, D, tol = 10**(-5), N = 10000):
  errors = []
  n = len(b)
  x0 = np.zeros(n)
  x = np.copy(x0)
  for k in range(0, N):
    for i in range(0, n):
      #summation1
      sum1 = 0.0
      for j in range(0, i): #range already doesnt do i, so this goes to i-1
        sum1 += A[i, j] * x[j]
      #summation2
      sum2 = 0.0
      for j in range(i + 1, n):
        sum2 += A[i, j] * x0[j]
      if abs(A[i,i]) <= 10**-16:
        return x, k, 0, 0
      x[i] = (-sum1 - sum2 + b[i])/A[i,i]
    error = (norm(x- x0))/(norm(x))
    if error < tol:
      df = pd.DataFrame(errors)
      df.to_csv("Errors_GaussSeidel_D=" + str(D) + ".csv")
      return x, k, 1, df
    errors.append([k, error])
    x0 = np.copy(x)
  return x, k, 0, 0



#https://www.youtube.com/watch?v=z9glsQDkkWU&t=782s
#psuedocode: https://www3.nd.edu/~zxu2/acms40390F12/Lec-7.3.pdf