# MILESTONE 1 Write a script to integrate Kepler Orbits with Euler, Crank-Nicolson and RK4 Method
# EULER

from numpy import array,zeros
import matplotlib.pyplot as plt

N = 10000
U = array( [1,0,0,1] )
dt = 0.001
x = array( zeros(N) )
y = array( zeros(N) )
x[0] = U[0] 
y[0] = U[1]

def F_Kepler(U):
   x , y , vx , vy = U[0] , U[1] , U[2] , U[3]
   mr = (x**2 + y**2)**1.5
   return array ( [vx , vy , -x/mr , -y/mr] )

for i in range(1,N):
    #F = array( [ U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5, -U[1]/(U[0]**2+U[1]**2)**1.5 ] ) 
    F = F_Kepler (U)
    U = U + dt*F
    x[i] = U[0]
    y[i] = U[1]

plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (EULER METHOD)')
plt.show()
