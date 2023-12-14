# Ejercicios clase de teoria.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

from ODEs.Cauchy_problem import Cauchy_problem, Cauchy_problem_3D
from ODEs.Temporal_Schemes import Euler, CN, RK4, Inverse_Euler, LF
from Physic.Physics import Kepler, Oscillator, Clase, Brusellator, Duffing0, Duffing1, Duffing2, VanderPol, Rayleigh, Lorentz,Rossler


# 1. PUNTO DE SILLA

# ------------------------------------------------------------------------------- #
#INPUTS CAUCHY:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # dt: time step
    # t : time partition t (vector of length N+1)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
# ------------------------------------------------------------------------------- #

# Introduce inputs: MANUALLY - BISECTRIZ
F = Clase
dt = 0.08
t = arange(0, 1.6, dt)
Uo = array([2/1.9, 1/1.9])
temporal_scheme = RK4
U, x1, y1 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs: MANUALLY - BISECTRIZ
F = Clase
dt = 0.08
t = arange(0, 1.6, dt)
Uo = array([-2/1.9, -1/1.9])
temporal_scheme = RK4
U, x3, y3 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs: MANUALLY - BISECTRIZ
F = Clase
dt = 0.1
t = arange(0, 5, dt)
Uo = array([8, 16])
temporal_scheme = RK4
U, x2, y2 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs: MANUALLY - BISECTRIZ
F = Clase
dt = 0.1
t = arange(0, 5, dt)
Uo = array([-8, -16])
temporal_scheme = RK4
U, x4, y4 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs: MANUALLY 
F = Clase
dt = 0.1
t = arange(0, 1.3, dt)
Uo = array([-6, -16])
temporal_scheme = RK4
U, x9, y9 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs: MANUALLY 
F = Clase
dt = 0.1
t = arange(0, 1.3, dt)
Uo = array([6, 16])
temporal_scheme = RK4
U, x10, y10 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs: MANUALLY 
F = Clase
dt = 0.1
t = arange(0, 1.9, dt)
Uo = array([9, 17])
temporal_scheme = RK4
U, x11, y11 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs: MANUALLY 
F = Clase
dt = 0.1
t = arange(0, 1.9, dt)
Uo = array([-9, -17])
temporal_scheme = RK4
U, x12, y12 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Plot
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x9,y9)
plt.plot(x10,y10)
plt.plot(x11,y11)
plt.plot(x12,y12)#need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
plt.show()
