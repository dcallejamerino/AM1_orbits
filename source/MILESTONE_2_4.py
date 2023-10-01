# MILESTONE 2 Write a function called Inverse_Euler to integrate one step
# Inverse Euler

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


def Inverse_Euler(U, dt, t, F): 

    def Residual(X): 
          return X - U - dt * F(X, t)

    return newton(func = Residual, x0 = U ) 


for i in range(1, N): 

      dt = 0.1 
      t[i] = dt*i
      U = Inverse_Euler (U, dt, t, Kepler)
      x[i] = U[0] 
      y[i] = U[1]


plt.plot(x, y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (INVERSE EULER METHOD)')
plt.show()  
