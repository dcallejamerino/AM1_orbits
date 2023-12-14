# MILESTONE 4

from numpy import array, zeros, float64, arange, transpose, linspace
from scipy.optimize import newton
import matplotlib.pyplot as plt

from ODEs.Cauchy_problem import Cauchy_problem
from ODEs.Temporal_Schemes import Euler, CN, RK4, Inverse_Euler, LF
from Physic.Physics import Kepler, Oscillator, Clase, Brusellator, Duffing0, Duffing1, Duffing2, VanderPol, Rayleigh, Lorentz,Rossler
from Stability.Stability_Regions import Stability_region

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

F = Oscillator
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([1, 0])
temporal_scheme = Euler
U, x1, y1 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs para INVERSE EULER: 

F = Oscillator
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([1, 0])
temporal_scheme = Inverse_Euler
U, x2, y2 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs para CN: 

F = Oscillator
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([1, 0])
temporal_scheme = CN
U, x3, y3 = Cauchy_problem(F, t, Uo, temporal_scheme)

# Introduce inputs para RK4: 

F = Oscillator
dt = 0.01
t = arange(0, 200, dt)    
Uo = array([1, 0])
temporal_scheme = RK4
U, x4, y4 = Cauchy_problem(F, t, Uo, temporal_scheme)


# # Introduce inputs para LF: 

def Cauchy_problem_LP(F, t, Uo, temporal_scheme):
    Nv = len(Uo)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((Nv, N + 1), dtype=float64)
    U[:, 0] = Uo
    U[:,1] = U[:,0] + dt*F(U[:,0], t[0])

    for i in range(1,N):
        U[:, i + 1] = temporal_scheme(U[:, i], U[:, i-1], t[i], t[i+1]-t[i], F)
        
    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row

    return U, x, y

F = Oscillator
dt = 0.01
t = arange(0, 200, dt)  
Uo = array([1, 0])
U1 = Uo + dt * F(Uo,t)
temporal_scheme = LF
U, x5, y5 = Cauchy_problem_LP(F, t, Uo, temporal_scheme)



# Plot 1
plt.plot(x1,y1,label='Euler')
plt.plot(x2,y2,label='Inverse_Euler')
plt.plot(x3,y3,label='CN')
plt.plot(x4,y4,label='RK4')
plt.plot(x5,y5,label='LF')


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
plt.plot(t,x5,label='LF')

plt.xlabel('t')
plt.ylabel('x') 
plt.ylim(-3, 3)
plt.grid()
plt.legend()
plt.title('Harmonic Oscillator with different schemes: time domain')
plt.show()





