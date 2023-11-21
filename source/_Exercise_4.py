# Ejercicios clase de teoria.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import Temporal_Schemes, Physics, Cauchy_problem

# 4. DUFFING para K=0.05 y B=1
# Introduce inputs: SISTEMA CAOTICO

F = Physics.Clase4
dt = 0.01
t = arange(500, 700, dt)  
Uo = array([0, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

F = Physics.Clase4
dt = 0.01
t = arange(500, 700, dt)  
Uo = array([0.1, 0.1])
temporal_scheme = Temporal_Schemes.RK4
U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)


# Plot
plt.plot(x1,y1)
plt.plot(x2,y2)

plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
plt.show()

# # # Plot t e x
# # plt.plot(t, x1)              #need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
# # plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
# # plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# # TS_name = temporal_scheme.__name__
# # F_name = F.__name__
# # plt.title('Cauchy function using {} temporal scheme, to resolve a {} being the initial conditions Uo {} and the time domain t={}  dt={}'.format(TS_name,F_name,Uo,t[-1],dt))
# # plt.show()