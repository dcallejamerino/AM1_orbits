# Write a function to integrate a Cauchy problem. Temporal scheme, initial condition and the function F(U, t) of the Cauchy problem should be input arguments.

from numpy import array, zeros, float64, arange
from scipy.optimize import newton
import matplotlib.pyplot as plt
import Temporal_Schemes, Physics

### CAUCHY ###
# ------------------------------------------------------------------------------- #
#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N+1)
    # dt: time step
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py

#RETURN:
    # U: matrix[Nv, N+1], Nv state values at N+1 time steps 
# ------------------------------------------------------------------------------- #

# # Cauchy 2D
def Cauchy_problem(F, t, Uo, temporal_scheme):
    Nv = len(Uo)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((Nv, N + 1), dtype=float64)
    U[:, 0] = Uo

    for i in range(N):
        U[:, i + 1] = temporal_scheme(U[:, i], t[i], t[i+1]-t[i], F)

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row

    return U, x, y  

# # CAUCHY 3D
def Cauchy_problem_3D(F, t, Uo, temporal_scheme):
    Nv = len(Uo)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((Nv, N + 1), dtype=float64)
    U[:, 0] = Uo

    for i in range(N):
        U[:, i + 1] = temporal_scheme(U[:, i], t[i], t[i+1]-t[i], F)

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row
    z = U[2, :]  # Collect y values or values of the 3rd row

    return U, x, y, z

