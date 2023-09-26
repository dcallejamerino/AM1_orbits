# 1. Write a script to integrate Kepler Orbits with an Euler Method

#     Un+1 = Un + dt * Fn
#     Where:
#          Un is the Status Vector (position and speed) in the instant "n": approximate solution
#          dt is the derivative
#          Fn is a function of the Status Vector (speed and -position/(position module)^3) in the instant "n"

# Calls
from numpy import array,zeros
import matplotlib.pyplot as plt

# Parameters
N = 100000
U = array( [1,0,0,1] )
dt = 0.0001
x = array( zeros(N) )
y = array( zeros(N) )
x[0] = U[0] 
y[0] = U[1]

# Function
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

# Result    
plt.plot(x,y)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Kepler Orbit (EULER-METHOD)')
plt.show()
