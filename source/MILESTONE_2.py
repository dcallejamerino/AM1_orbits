# MILESTONE 2 why 
#Integration of Kepler into different methods

from numpy import array, zeros
import numpy as np
from scipy.optimize import newton
import matplotlib.pyplot as plt
import Temporal_Schemes, Physics, Cauchy_problem

# 7. Integrate a Kepler with these latter schemes and explain the results


# 7.1 Kepler with Euler method & print

U = array( [1,0,0,1] ) # Initial value of U

N = 10000
dt = 0.01

x = array( zeros(N) )
y = array( zeros(N) )
t = array( zeros(N) )

x[0] = U[0] 
y[0] = U[1]
t[0] = 0

for i in range(1, N): 
      t[i] = dt*i
      U = Temporal_Schemes.Euler (U, t, dt, Physics.Kepler)
      x[i] = U[0] 
      y[i] = U[1]
      
plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (EULER METHOD) for N={} and dt={}'.format(N,dt))
plt.show()


# 7.2 Kepler with CN method & print

U = array( [1,0,0,1] ) # Initial value of U

N = 100
dt = 0.1

x = array( zeros(N) )
y = array( zeros(N) )
t = array( zeros(N) )

x[0] = U[0] 
y[0] = U[1]
t[0] = 0

for i in range(1, N): 
      t[i] = dt*i
      U = Temporal_Schemes.CN (U, t, dt, Physics.Kepler)
      x[i] = U[0] 
      y[i] = U[1]
      
plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (CN METHOD) for N={} and dt={}'.format(N,dt))
plt.show()


# 7.3 Kepler with RK4 method & print

U = array( [1,0,0,1] ) # Initial value of U

N = 100
dt = 0.1

x = array( zeros(N) )
y = array( zeros(N) )
t = array( zeros(N) )

x[0] = U[0] 
y[0] = U[1]
t[0] = 0

for i in range(1, N): 
      t[i] = dt*i
      U = Temporal_Schemes.RK4 (U, t, dt, Physics.Kepler)
      x[i] = U[0] 
      y[i] = U[1]
      
plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (RK4 METHOD) for N={} and dt={}'.format(N,dt))
plt.show()


# 7.4 Kepler with Inverse Euler method & print

U = array( [1,0,0,1] ) # Initial value of U

N = 25
dt = 0.1

x = array( zeros(N) )
y = array( zeros(N) )
t = array( zeros(N) )

x[0] = U[0] 
y[0] = U[1]
t[0] = 0

for i in range(1, N): 
      t[i] = dt*i
      U = Temporal_Schemes.Inverse_Euler (U, t, dt, Physics.Kepler)
      x[i] = U[0] 
      y[i] = U[1]
      
plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (Inverse Euler METHOD) for N={} and dt={}'.format(N,dt))
plt.show()

# 8. Increase and decrease the time step and explained the results
# Refer to Milestone 1
