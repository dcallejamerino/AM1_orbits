# MILESTONE 4

from numpy import array, zeros, float64, arange, transpose, linspace
from scipy.optimize import newton
import matplotlib.pyplot as plt
import Temporal_Schemes, Physics, Cauchy_problem, Stability_Regions

# 1. Integrate the linear oscillator with some initial conditions

# ------------------------------------------------------------------------------- #
#INPUTS CAUCHY:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # dt: time step
    # t : time partition t (vector of length N+1)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
# ------------------------------------------------------------------------------- #

# Introduce inputs para EULER: 

F = Physics.Oscillator
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([1, 0])
temporal_scheme = Temporal_Schemes.Euler
U, x1, y1 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs para INVERSE EULER: 

F = Physics.Oscillator
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([1, 0])
temporal_scheme = Temporal_Schemes.Inverse_Euler
U, x2, y2 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs para CN: 

F = Physics.Oscillator
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([1, 0])
temporal_scheme = Temporal_Schemes.CN
U, x3, y3 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs para RK4: 

F = Physics.Oscillator
dt = 0.01
t = arange(0, 200, dt)    
Uo = array([1, 0])
temporal_scheme = Temporal_Schemes.RK4
U, x4, y4 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# # Introduce inputs para LF: 

# F = Physics.Oscillator
# dt = 0.01
# t = arange(0, 200, dt)  
# Uo = array([1, 0])
# U1 = Uo + dt * F(Uo,t)
# temporal_scheme = Temporal_Schemes.LF
# U, x5, y5 = Cauchy_problem.Cauchy_problem(F, t, Uo, temporal_scheme)

# Plot 1
plt.plot(x1,y1,label='Euler')
plt.plot(x2,y2,label='Inverse_Euler')
plt.plot(x3,y3,label='CN')
plt.plot(x4,y4,label='RK4')


plt.xlabel('x')
plt.ylabel('y') 
plt.axis('equal')
plt.grid()
plt.legend()
plt.title('Harmonic Oscillator with different schemes')
plt.show()

# Plot 2
plt.plot(t,x1,label='Euler')
plt.plot(t,x2,label='Inverse_Euler')
plt.plot(t,x3,label='CN')
plt.plot(t,x4,label='RK4')

plt.xlabel('t')
plt.ylabel('x') 
plt.ylim(-3, 3)
plt.grid()
plt.legend()
plt.title('Harmonic Oscillator with different schemes: time domain')
plt.show()





