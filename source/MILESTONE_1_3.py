# 3. Write a script to integrate Kepler Orbits with an Runge-Kutta 4th Order Method
from numpy import array, zeros, linspace
import matplotlib.pyplot as plt

U = array( [ 1, 0, 0, 1 ])
    
N = 100000 
dt = 0.0001
x = array( zeros(N) )
y = array( zeros(N) )
x[0] = U[0] 
y[0] = U[1]
def F_Kepler(U):
   x , y , vx , vy = U[0] , U[1] , U[2] , U[3]
   mr = (x**2 + y**2)**1.5
   return array ( [vx , vy , -x/mr , -y/mr] )
    
for i in range(1, N): 
    F = F_Kepler(U)
    Y1 = F
    Y2 = F+0.5*dt*Y1
    Y3 = F+0.5*dt*Y2
    Y4 = F+dt*Y3
    U = U + dt/6*(Y1+2*Y2+2*Y3+Y4) 
    x[i] = U[0] 
    y[i] = U[1]
    
plt.plot(x, y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (RUNGE-KUTTA 4 METHOD)')
plt.show()  
