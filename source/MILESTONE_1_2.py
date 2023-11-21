# MILESTONE 1 Write a script to integrate Kepler Orbits with Crank-Nicolson
# 2. Crank-Nicolson

from numpy import array, zeros
from scipy.optimize import newton
import matplotlib.pyplot as plt
  
  
U = array( [ 1, 0, 0, 1 ])
    
N = 100
x = array( zeros(N) )
y = array( zeros(N) )
t = array( zeros(N) )

x[0] = U[0] 
y[0] = U[1]
t[0] = 0 
    
def Kepler(U, t): 

    x = U[0]; y = U[1]; dxdt = U[2]; dydt = U[3]
    d = ( x**2  +y**2 )**1.5

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 


def CN (U, dt, t, F ): 

    def Residual_CN(X): 
         
         return  X - a - dt/2 *  F(X, t + dt)

    a = U  +  dt/2 * F(U, t) 
    
    return newton( Residual_CN, U )

for i in range(1, N): 

      dt = 0.1 
      t[i] = dt*i
      U = CN (U, dt, t, Kepler)
      x[i] = U[0] 
      y[i] = U[1]


plt.plot(x, y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (CN METHOD) for N={} and dt={}'.format(N,dt))
plt.show()  

