
# Prototype to integrate a Kepler orbit 
from  numpy import array, split, concatenate, append, zeros, reshape, linspace,float64,log10, ones, vstack, arange
from numpy.linalg import norm, lstsq
import matplotlib.pyplot as plt
from time import process_time
import Test1



def F_Kepler(U, t): 

    x = U[0]; y = U[1]; dxdt = U[2]; dydt = U[3]
    d = ( x**2  +y**2 )**1.5

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 

def Euler( U, dt, t, F): 

   return U + dt * F( U, t ) 


dt = 0.01
t = arange(0, 200, dt)  
U0 = array( [1, 0, 0, 1 ] )
order = 1 

print("Error Kepler orbit ") 
Error1 = Test1.Error_Cauchy_Problem( t, F_Kepler,  Euler, order, U0 )

plt.plot(t, Error1[:,0] )
plt.axis('equal')
plt.grid()
plt.show()


        
 
N = 2000
t = linspace(0, 10, N) 
U0 = array( [1, 0, 0, 1 ] )
m = 5

print("Order Euler ") 
log_e1, log_n1 = Test1.Temporal_convergence_rate( t, F_Kepler, U0, Euler, m )

print( "order =", order)
plt.plot(log_n1, log_e1 )
plt.axis('equal')
plt.grid()
plt.show()



