# Ejercicios clase de teoria.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import Temporal_Schemes, Physics, Cauchy_problem


# 2. BRUSELLATOR

# ------------------------------------------------------------------------------- #
#INPUTS CAUCHY:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # dt: time step
    # t : time partition t (vector of length N+1)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
# ------------------------------------------------------------------------------- #

# # Introduce inputs
F = Physics.Brusellator
dt = 0.1
t = arange(0, 1000, dt)  
Uo = array([1.125, 1.874])
temporal_scheme = Temporal_Schemes.RK4
U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# Plot x e y
plt.plot(x1,y1)
plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve {}'.format(TS_name,F_name))
plt.show()

# Plot t e x
plt.plot(t, x1)              #need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve {} being the initial conditions Uo {} and the time domain t={}  dt={}'.format(TS_name,F_name,Uo,t[-1],dt))
plt.show()