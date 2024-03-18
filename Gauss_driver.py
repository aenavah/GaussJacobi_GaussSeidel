import numpy as np
import matplotlib.pyplot as plt

import Gauss_functions
GaussJacobi = Gauss_functions.GaussJacobi
GaussSeidel = Gauss_functions.GaussSeidel

if __name__ == "__main__":

  m = int(input("Input m for matrix size mxm: "))
  D = int(input("Input value of d_{ii}: "))
  A = np.ones((m, m))
  np.fill_diagonal(A, D)
  b = []
  for i in range(0, m):
    b.append(i+1)
  which = int(input("To solve Ax = b enter (0) Gauss-Jacobi or (1) Gauss-Seidel: "))
  sol0, iterations0, works0, errors_df0 = GaussJacobi(A, b, D)
  sol1, iterations1, works1, errors_df1 = GaussSeidel(A, b, D)
  if which == 0:
    print("Using Gauss-Jacobi Method...")
    if works0 == 1:
      print("Yippee!")
      print(sol0)
    else:
      print("Booooo!")

    print(sol0)
  if which == 1:
    print("Using Gauss-Seidel Method...")
    if works1 == 1:
      print("Yippee!")
      print(sol1)
    else:
      print("Booooo!")

  # if ((works0 == 1) and (works1 == 1)):
  #   print("Plotting both...")
  #   errors_df0.plot(x=0, y=1, kind="line", marker='o', color="pink", label="Gauss-Jacobi")
  #   errors_df1.plot(x=0, y=1, kind="line", marker='o', color="lightblue", label="Gauss-Seidel")
  # if (works0 == 1) ^ (works1 == 1): 
  #   print("Plotting...")
  #   if works0 == 1:
  #     errors_df0.plot(x=0, y=1, kind="line", marker='o', color="pink", label="Gauss-Jacobi")
  #   if works1 == 1:
  #     errors_df1.plot(x=0, y=1, kind="line", marker='o', color="lightblue", label="Gauss-Seidel")
  #   plt.xlabel("Iteration number")
  #   plt.ylabel("Error")
  #   plt.title("Error(Iteration Number)")
  #   plt.savefig("errors_D=" + str(D) + ".jpg")
    
  if works0 == 1 or works1 == 1:
      ax = None
      if works0 == 1:
          ax = errors_df0.plot(x=0, y=1, kind="line", marker='o', color="pink", label="Gauss-Jacobi")
      if works1 == 1:
          ax = errors_df1.plot(x=0, y=1, kind="line", marker='o', color="lightblue", label="Gauss-Seidel", ax=ax)
      ax.set_xlabel("Iteration number")
      ax.set_ylabel("Error")
      ax.set_title("Error vs Iteration Number")
      plt.savefig("errors_D=" + str(D) + ".jpg")
      plt.show()

