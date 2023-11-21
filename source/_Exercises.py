# Ejercicios clase de teoria.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import Temporal_Schemes, Physics, Cauchy_problem


# # 1. PUNTO DE SILLA
# # Introduce inputs: MANUALLY - BISECTRIZ
# F = Physics.Clase
# t = np.linspace(0, 20, 21)  # Assuming you want to create a time vector from 0 to 20
# dt = 0.08
# Uo = array([2/1.9, 1/1.9])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs: MANUALLY - BISECTRIZ
# F = Physics.Clase
# t = np.linspace(0, 20, 21)  # Assuming you want to create a time vector from 0 to 20
# dt = 0.08
# Uo = array([-2/1.9, -1/1.9])
# temporal_scheme = Temporal_Schemes.RK4
# U, x3, y3 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs: MANUALLY - BISECTRIZ
# F = Physics.Clase
# t = np.linspace(0, 50, 51)  # Assuming you want to create a time vector from 0 to 50
# dt = 0.1
# Uo = array([8, 16])
# temporal_scheme = Temporal_Schemes.RK4
# U, x2, y2 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs: MANUALLY - BISECTRIZ
# F = Physics.Clase
# t = np.linspace(0, 50, 51)  # Assuming you want to create a time vector from 0 to 50
# dt = 0.1
# Uo = array([-8, -16])
# temporal_scheme = Temporal_Schemes.RK4
# U, x4, y4 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs: MANUALLY 
# F = Physics.Clase
# t = np.linspace(0, 13, 14)  # Assuming you want to create a time vector from 0 to 13
# dt = 0.1
# Uo = array([-6, -16])
# temporal_scheme = Temporal_Schemes.RK4
# U, x9, y9 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs: MANUALLY 
# F = Physics.Clase
# t = np.linspace(0, 13, 14)  # Assuming you want to create a time vector from 0 to 13
# dt = 0.1
# Uo = array([6, 16])
# temporal_scheme = Temporal_Schemes.RK4
# U, x10, y10 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs: MANUALLY 
# F = Physics.Clase
# t = np.linspace(0, 19, 20)  # Assuming you want to create a time vector from 0 to 19
# dt = 0.1
# Uo = array([9, 17])
# temporal_scheme = Temporal_Schemes.RK4
# U, x11, y11 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs: MANUALLY 
# F = Physics.Clase
# t = np.linspace(0, 19, 20)  # Assuming you want to create a time vector from 0 to 19
# dt = 0.1
# Uo = array([-9, -17])
# temporal_scheme = Temporal_Schemes.RK4
# U, x12, y12 = Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Plot
# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.plot(x3,y3)
# plt.plot(x4,y4)
# plt.plot(x9,y9)
# plt.plot(x10,y10)
# plt.plot(x11,y11)
# plt.plot(x12,y12)#need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
# plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()


# # 2. BRUSELLATOR
# # Introduce inputs
# F = Physics.Clase2
# t = np.linspace(500, 1000, 1001)  # Assuming you want to create a time vector from 0 to 20
# dt = 0.1
# Uo = array([1.125, 1.874])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Plot x e y
# plt.plot(x1,y1)
# plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()

# # Plot t e x
# plt.plot(t, x1)              #need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
# plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {} being the initial conditions Uo {} and the time domain t={}  dt={}'.format(TS_name,F_name,Uo,t[-1],dt))
# plt.show()

# # # 3. DUFFING
# # # Introduce inputs
# F = Physics.Clase3
# dt = 0.1
# t = arange(0, 1000, dt)  
# Uo = array([0, 0])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# F = Physics.Clase3
# dt = 0.1
# t = arange(0, 1000, dt)  
# Uo = array([0.2, 0.2])
# temporal_scheme = Temporal_Schemes.RK4
# U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# F = Physics.Clase3
# dt = 0.1
# t = arange(0, 1000, dt)  
# Uo = array([0.5, 0.5])
# temporal_scheme = Temporal_Schemes.RK4
# U, x3, y3 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# F = Physics.Clase3
# dt = 0.1
# t = arange(0, 1000, dt)  
# Uo = array([1.5, 1.5])
# temporal_scheme = Temporal_Schemes.RK4
# U, x4, y4 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# F = Physics.Clase3
# dt = 0.1
# t = arange(0, 1000, dt)  
# Uo = array([2, 2])
# temporal_scheme = Temporal_Schemes.RK4
# U, x5, y5 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Plot
# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.plot(x3,y3)
# plt.plot(x4,y4)
# plt.plot(x5,y5)

# plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()

# # 4. DUFFING para K=0.05 y B=1
# # Introduce inputs: SISTEMA CAOTICO

# F = Physics.Clase4
# dt = 0.01
# t = arange(500, 700, dt)  
# Uo = array([0, 0])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# F = Physics.Clase4
# dt = 0.01
# t = arange(500, 700, dt)  
# Uo = array([0.1, 0.1])
# temporal_scheme = Temporal_Schemes.RK4
# U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)


# # Plot
# plt.plot(x1,y1)
# plt.plot(x2,y2)

# plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()

# # # # Plot t e x
# # # plt.plot(t, x1)              #need to select MANUALLY what we want to plot, will depend on the Physics (2 or 4 values? against t?)
# # # plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
# # # plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# # # TS_name = temporal_scheme.__name__
# # # F_name = F.__name__
# # # plt.title('Cauchy function using {} temporal scheme, to resolve a {} being the initial conditions Uo {} and the time domain t={}  dt={}'.format(TS_name,F_name,Uo,t[-1],dt))
# # # plt.show()

# # 5. DUFFING para K=0.001 y B=1
# # Introduce inputs: SISTEMA CAOTICO: atractor extrano. Cuando mayor es K mas se parecen los sistemas, sin embargo, sigue siendo un sistema caotico

# F = Physics.Clase5
# dt = 0.01
# t = arange(0, 200, dt)  
# Uo = array([0, 0])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# F = Physics.Clase5
# dt = 0.01
# t = arange(0, 200, dt)  
# Uo = array([0.1, 0.1])
# temporal_scheme = Temporal_Schemes.RK4
# U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)


# # # Plot x e y
# # plt.plot(x1,y1)
# # plt.plot(x2,y2)

# # plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# # plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# # TS_name = temporal_scheme.__name__
# # F_name = F.__name__
# # plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# # plt.show()

# # Plot x y t
# plt.plot(t,x1)
# plt.plot(t,x2)

# plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('t Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()


# # 6. VAN DER POL - CICLO LIMITE
# # Introduce inputs: 

# F = Physics.Clase6
# dt = 0.01
# t = arange(0, 400, dt)  
# Uo = array([1.7, 1.1])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Plot x e y
# plt.plot(x1,y1)

# plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()

# # 7. RAYLEIGH - CICLO LIMITE
# # Introduce inputs: 

# F = Physics.Clase7
# dt = 0.01
# t = arange(0, 300, dt)  
# Uo = array([0, 0])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# F = Physics.Clase7
# dt = 0.01
# t = arange(0, 300, dt)  
# Uo = array([1, 0])
# temporal_scheme = Temporal_Schemes.RK4
# U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# # Plot x e t
# #plt.plot(t,x2)
# plt.plot( x2 , y2, "." )


# plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()


# # 8. LORENTZ 
# # Introduce inputs para primera condicion inicial: 

# F = Physics.Clase8
# dt = 0.01
# t = arange(0, 50, dt)  
# Uo = array([3, 3, 3])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1, z1 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs para segunda condicion inicial: 

# F = Physics.Clase8
# dt = 0.01
# t = arange(0, 50, dt)  
# Uo = array([6, 6, 6])
# temporal_scheme = Temporal_Schemes.RK4
# U, x2, y2, z2 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

# # Plot 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x1, y1, z1, label='Uo = ([3, 3, 3])')
# ax.plot(x2, y2, z2, label='Uo = ([6, 6, 6])')
# # Establecer etiquetas para los ejes
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# # Mostrar la leyenda
# ax.legend()
# # Plot 3D
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()

# # Plot 2D: x e t
# plt.plot(t,x1)
# plt.plot(t,x2)
# plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()


# # 9. ROSSLER
# # Introduce inputs para primera condicion inicial: 

# F = Physics.Clase9
# dt = 0.01
# t = arange(0, 200, dt)  
# Uo = array([-1, 1, 1])
# temporal_scheme = Temporal_Schemes.RK4
# U, x1, y1, z1 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

# # Introduce inputs para segunda condicion inicial: 

# F = Physics.Clase9
# dt = 0.01
# t = arange(0, 200, dt)  
# Uo = array([0, 0, 0])
# temporal_scheme = Temporal_Schemes.RK4
# U, x2, y2, z2 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

# # Plot 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x1, y1, z1, label='Uo = ([-1, 1, 1])')
# ax.plot(x2, y2, z2, label='Uo = ([0, 0, 0])')
# # Establecer etiquetas para los ejes
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# # Mostrar la leyenda
# ax.legend()
# # Plot 3D
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()

# # Plot 2D: x e t
# plt.plot(t,x1)
# plt.plot(t,x2)
# plt.xlabel('t Position')    #take 1st argument MANUALLY from previous line (for the description)
# plt.ylabel('x Position')    #take 2nd argument MANUALLY from previous line  (for the description)
# TS_name = temporal_scheme.__name__
# F_name = F.__name__
# plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
# plt.show()

# 9. ROSSLER ANIMATED
# Introduce inputs para primera condicion inicial: 

F = Physics.Clase9
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([-1, 1, 1])
temporal_scheme = Temporal_Schemes.RK4
U, x1, y1, z1 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

# Introduce inputs para segunda condicion inicial: 

F = Physics.Clase9
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([0, 0, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x2, y2, z2 = Cauchy_problem.Cauchy_problem_3D(F, t, dt, Uo, temporal_scheme)

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

