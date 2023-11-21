# Ejercicios clase de teoria.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import Temporal_Schemes, Physics, Cauchy_problem

# 8. LORENTZ 
# Introduce inputs para primera condicion inicial: 

F = Physics.Clase8
dt = 0.01
t = arange(0, 50, dt)  
Uo = array([3, 3, 3])
temporal_scheme = Temporal_Schemes.RK4
U, x1, y1, z1 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

# Introduce inputs para segunda condicion inicial: 

F = Physics.Clase8
dt = 0.01
t = arange(0, 50, dt)  
Uo = array([6, 6, 6])
temporal_scheme = Temporal_Schemes.RK4
U, x2, y2, z2 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

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
plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
plt.show()

# Plot 2D: x e t
plt.plot(t,x1)
plt.plot(t,x2)
plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
plt.show()