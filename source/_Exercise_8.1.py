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
# Creamos lineas vacias para comenzar la animacion
line1, = ax.plot([], [], [], label='Uo = [3, 3, 3]')
line2, = ax.plot([], [], [], label='Uo = [6, 6, 6]')
# Establecer etiquetas para los ejes
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
# Ajustar los limites de cada eje
ax.set_xlim(min(x1), max(x1))
ax.set_ylim(min(y1), max(y1))
ax.set_zlim(min(z1), max(z1))
# Mostrar la leyenda
ax.legend()
# Plot 3D
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# Function to initialize the plot
def init():
    line1.set_data([], [])
    line1.set_3d_properties([])
    line2.set_data([], [])
    line2.set_3d_properties([])
    return line1, line2

# Function to update the plot for each animation frame
def update(frame):
    x1_, y1_, z1_ = x1[:frame], y1[:frame], z1[:frame]
    x2_, y2_, z2_ = x2[:frame], y2[:frame], z2[:frame]

    line1.set_data(x1_, y1_)
    line1.set_3d_properties(z1_)

    line2.set_data(x2_, y2_)
    line2.set_3d_properties(z2_)

    return line1, line2

# Create the animation
animation = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1)


plt.show()
