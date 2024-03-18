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

  if which == 1:
    print("Using Gauss-Seidel Method...")
    if works1 == 1:
      print("Yippee!")
      print(sol1)
    else:
      print("Booooo!")

  if works0 == 1 or works1 == 1:
    ax = None
    if works0 == 1:
      ax = errors_df0.plot(x=0, y=1, kind="line", marker='o', color="pink", label="Gauss-Jacobi")
    if works1 == 1:
      ax = errors_df1.plot(x=0, y=1, kind="line", marker='o', color="lightblue", label="Gauss-Seidel", ax=ax)
    ax.set_xlabel("Iteration number")
    ax.set_ylabel("Error")
    ax.set_title("Error vs Iteration Number for D = " + str(D))
    plt.savefig("errors_D=" + str(D) + ".jpg")

    A20 = np.ones((10, 10))
    D20 = [1,2,3,4,5,6,7,8,9,10]
    b20 = D20.copy()
    np.fill_diagonal(A20, D20)
    #print(A20)
    sol20, tmp, tmp, tmp = GaussJacobi(A20, b20, "finalpart")
    A21 = np.ones((10, 10))
    D21 = [1,2,3,4,5,6,7,8,9,10]
    b21 = D21.copy()
    np.fill_diagonal(A21, D21)
    #print(A21)
    sol21, tmp, tmp, tmp = GaussSeidel(A21, b21, "finalpart")
    print(sol20)
    print(sol21)


