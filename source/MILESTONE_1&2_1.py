# MILESTONE 1&2 Write a script to integrate Kepler Orbits with Euler, Crank-Nicolson and RK4 Method
# EULER

from numpy import array,zeros
import matplotlib.pyplot as plt

U = array( [1,0,0,1] )

N = 10000
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


def Euler(U, dt, t, F ): 
    
    return  U + dt * F(U,t)


for i in range(1, N): 

      dt = 0.01 
      t[i] = dt*i
      U = Euler (U, dt, t, Kepler)
      x[i] = U[0] 
      y[i] = U[1]

plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (EULER METHOD)')
plt.show()

## Old version before moving to time domain
# for i in range(1,N):
#     #F = array( [ U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5, -U[1]/(U[0]**2+U[1]**2)**1.5 ] ) 
#     F = F_Kepler (U)
#     U = U + dt*F
#     x[i] = U[0]
#     y[i] = U[1]