# MILESTONE 2

from numpy import array, zeros
from scipy.optimize import newton
import matplotlib.pyplot as plt
from ODEs.Temporal_Schemes import Euler, CN, RK4, Inverse_Euler, LF
from Physic.Physics import Kepler, Oscillator, Clase, Brusellator, Duffing0, Duffing1, Duffing2, VanderPol, Rayleigh, Lorentz,Rossler


# 1. Write a function called Euler to integrate one step: Refer to Temporal_Schemes

# 2. Write a function called Crank_Nicolson to integrate one step: Refer to Temporal_Schemes

# 3. Write a function called RK4 to integrate one step: Refer to Temporal_Schemes

# 4. Write a function called Inverse_Euler to integrate one step: Refer to Temporal_Schemes

# 5. Write a function to integrate a Cauchy problem: Refer to Cauchy_problem

# 6. Write a function to express the force of the Kepler movement: Refer to Physics

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
      U = Euler (U, t, dt, Kepler)
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
      U = CN (U, t, dt, Kepler)
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
      U = RK4 (U, t, dt, Kepler)
      x[i] = U[0] 
      y[i] = U[1]
      
plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (RK4 METHOD) for N={} and dt={}'.format(N,dt))
plt.show()


# 7.4 Kepler with Inverse Euler method & print

U = array( [1,0,0,1] ) # Initial value of U

N = 20
dt = 0.1

x = array( zeros(N) )
y = array( zeros(N) )
t = array( zeros(N) )

x[0] = U[0] 
y[0] = U[1]
t[0] = 0

for i in range(1, N): 
      t[i] = dt*i
      U = Inverse_Euler (U, t, dt, Kepler)
      x[i] = U[0] 
      y[i] = U[1]
      
plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (Inverse Euler METHOD) for N={} and dt={}'.format(N,dt))
plt.show()

# 8. Increase and decrease the time step and explained the results
# Refer to Milestone 1
