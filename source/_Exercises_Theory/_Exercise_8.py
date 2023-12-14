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

# 8. LORENTZ 
# ------------------------------------------------------------------------------- #
#INPUTS CAUCHY:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # dt: time step
    # t : time partition t (vector of length N+1)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
# ------------------------------------------------------------------------------- #

# Introduce inputs para primera condicion inicial: 

F = Lorentz
dt = 0.01
t = arange(0, 50, dt)  
Uo = array([3, 3, 3])
temporal_scheme = RK4
U, x1, y1, z1 = Cauchy_problem_3D(F, t, Uo, temporal_scheme)

# Introduce inputs para segunda condicion inicial: 

F = Lorentz
dt = 0.01
t = arange(0, 50, dt)  
Uo = array([6, 6, 6])
temporal_scheme = RK4
U, x2, y2, z2 = Cauchy_problem_3D(F, t, Uo, temporal_scheme)

# Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, z1, label='Uo = ([3, 3, 3])')
ax.plot(x2, y2, z2, label='Uo = ([6, 6, 6])')
# Establecer etiquetas para los ejes
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
# Mostrar la leyenda
ax.legend()
# Plot 3D
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve {}'.format(TS_name,F_name))
plt.show()

# Plot 2D: x e t
plt.plot(t,x1)
plt.plot(t,x2)
plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve {}'.format(TS_name,F_name))
plt.show()