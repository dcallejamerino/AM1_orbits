# Ejercicios clase de teoria.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import Temporal_Schemes, Physics, Cauchy_problem

# 9. ROSSLER ANIMATED
# ------------------------------------------------------------------------------- #
#INPUTS CAUCHY:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # dt: time step
    # t : time partition t (vector of length N+1)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
# ------------------------------------------------------------------------------- #

# Introduce inputs para primera condicion inicial: 

F = Physics.Rossler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([-1, 1, 1])
temporal_scheme = Temporal_Schemes.RK4
U, x1, y1, z1 = Cauchy_problem.Cauchy_problem_3D(F, t, Uo, temporal_scheme)

# Introduce inputs para segunda condicion inicial: 

F = Physics.Rossler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([0, 0, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x2, y2, z2 = Cauchy_problem.Cauchy_problem_3D(F, t, Uo, temporal_scheme)

# Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Creamos lineas vacias para comenzar la animacion
line1, = ax.plot([], [], [], label='Uo = [-1, 1, 1]')
line2, = ax.plot([], [], [], label='Uo = [0, 0, 0]')
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
plt.title('Cauchy function using {} temporal scheme, to resolve {}'.format(TS_name,F_name))
# Funcion para iniciar el plot
def init():
    line1.set_data([], [])
    line1.set_3d_properties([])
    line2.set_data([], [])
    line2.set_3d_properties([])
    return line1, line2

# Funcion para animar el plot
def update(frame):
    x1_, y1_, z1_ = x1[:frame], y1[:frame], z1[:frame]
    x2_, y2_, z2_ = x2[:frame], y2[:frame], z2[:frame]

    line1.set_data(x1_, y1_)
    line1.set_3d_properties(z1_)

    line2.set_data(x2_, y2_)
    line2.set_3d_properties(z2_)

    return line1, line2

# Crear animacion
animation = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1)


plt.show()
