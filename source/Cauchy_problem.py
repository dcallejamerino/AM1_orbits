# Write a function to integrate a Cauchy problem. Temporal scheme, initial condition and the function F(U, t) of the Cauchy problem should be input arguments.

from numpy import array, zeros, float64
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
import Temporal_Schemes, Physics

#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N+1)
    # dt: time step
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py

#RETURN:
    # U: matrix[Nv, N+1], Nv state values at N+1 time steps 


# # Cauchy 2D
def Cauchy_problem(F, t, dt, Uo, temporal_scheme):
    Nv = len(Uo)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((Nv, N + 1), dtype=float64)
    U[:, 0] = Uo

    for i in range(N):
        U[:, i + 1] = temporal_scheme(U[:, i], t[i], dt, F)

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 1st row

    return U, x, y  # Return the U matrix and x & y values (please note that depending on U, they may not mean x and y, maybe x and dx/dt)

# # CAUCHY 3D
# Cauchy
def Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme):
    Nv = len(Uo)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((Nv, N + 1), dtype=float64)
    U[:, 0] = Uo

    for i in range(N):
        U[:, i + 1] = temporal_scheme(U[:, i], t[i], dt, F)

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row
    z = U[2, :]  # Collect y values or values of the 2nd row

    return U, x, y, z


#Let's test it:

# #1. OSCILLATOR
# # Introduce inputs: MANUALLY
# F = Physics.Oscillator
# t = np.linspace(0, 1000, 1001)  # Assuming you want to create a time vector from 0 to 1000
# dt = 0.1
# Uo = array([1, 0])
# temporal_scheme = Temporal_Schemes.CN

# # Call the Cauchy_problem function
# U, x, y = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Plot x e y
# plt.plot(x, y)              #need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
# plt.xlabel('X Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('Y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {} being the initial conditions Uo {} and the time domain t={}  dt={}'.format(TS_name,F_name,Uo,t[-1],dt))
# plt.show()

# # Plot t e x
# plt.plot(t, x)              #need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
# plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {} being the initial conditions Uo {} and the time domain t={}  dt={}'.format(TS_name,F_name,Uo,t[-1],dt))
# plt.show()

