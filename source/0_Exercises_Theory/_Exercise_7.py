# Ejercicios clase de teoria.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import Temporal_Schemes, Physics, Cauchy_problem

# 7. RAYLEIGH - CICLO LIMITE
# ------------------------------------------------------------------------------- #
#INPUTS CAUCHY:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # dt: time step
    # t : time partition t (vector of length N+1)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
# ------------------------------------------------------------------------------- #

# Introduce inputs primera CI: 
F = Physics.Rayleigh
dt = 0.01
t = arange(0, 300, dt)  
Uo = array([0, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs segunda CI: 
F = Physics.Rayleigh
dt = 0.01
t = arange(0, 300, dt)  
Uo = array([1, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# Plot
#plt.plot(t,x2)
plt.plot( x2 , y2, "." )
plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve {}'.format(TS_name,F_name))
plt.show()
