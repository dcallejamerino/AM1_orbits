# 2. Write a script to integrate Kepler Orbits with a Crank-Nicolson Method
from numpy import array, zeros, linspace
from spicy.optimize import fsolve
import matplotlib.pyplot as plt

U = array( [ 1, 0, 0, 1 ])
  
N = 10000
dt = 0.01
x = array( zeros(N) )
y = array( zeros(N) )
U1_2 = array(zeros(N))  
x[0] = U[0] 
y[0] = U[1]
def F_Kepler(U):
   x , y , vx , vy = U[0] , U[1] , U[2] , U[3]
   mr = (x**2 + y**2)**1.5
   return array ( [vx , vy , -x/mr , -y/mr] )

def CN( DT , U , N):
    
    for i in range(N): 
        def CN_res(x):
            
            return x - U_temp - dt/2 * F_Kepler(x)
      
        U_temp = U[:,i] + dt/2 * F_Kepler(U[:,i])
        U[:,i] = fsolve(CN_res,U[:,i])
    return U


plt.plot(x, y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (CN METHOD)')
plt.show()  
