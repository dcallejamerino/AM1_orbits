# Write a function to integrate a Cauchy problem. Temporal scheme, initial condition and the function F(U, t) of the Cauchy problem should be input arguments.

from numpy import array, zeros, float64, arange
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
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


# # 6. VAN DER POEL - CICLO LIMITE
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

# 7. RAYLEIGH - CICLO LIMITE
# Introduce inputs: 

F = Physics.Clase7
dt = 0.01
t = arange(0, 300, dt)  
Uo = array([0, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

F = Physics.Clase7
dt = 0.01
t = arange(0, 300, dt)  
Uo = array([1, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, dt, Uo, temporal_scheme)

# Plot x e t
#plt.plot(t,x2)
plt.plot( x2 , y2, "." )


plt.xlabel('x Position')    #take 1st argument MANUALLY from previous line (for the description)
plt.ylabel('y Position')    #take 2nd argument MANUALLY from previous line  (for the description)
TS_name = temporal_scheme.__name__
F_name = F.__name__
plt.title('Cauchy function using {} temporal scheme, to resolve a {}'.format(TS_name,F_name))
plt.show()