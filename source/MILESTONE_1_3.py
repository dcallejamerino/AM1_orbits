# MILESTONE 1&2 Write a script to integrate Kepler Orbits with  RK4 Method
# 3. RK4

from numpy import array, zeros
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


def RK4(U, dt, t, F ): 

     k1 = F( U, t)
     k2 = F( U + dt * k1/2, t + dt/2 )
     k3 = F( U + dt * k2/2, t + dt/2 )
     k4 = F( U + dt * k3,   t + dt   )
 
     return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6

for i in range(1, N): 

      dt = 0.1 
      t[i] = dt*i
      U = RK4 (U, dt, t, Kepler)
      x[i] = U[0] 
      y[i] = U[1]

plt.plot(x, y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (RK4 METHOD) for N={} and dt={}'.format(N,dt))
plt.show()  
