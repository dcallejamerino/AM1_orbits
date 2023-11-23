
# Prototype to integrate a Kepler orbit 
from  numpy import array, split, concatenate, append, zeros, reshape, linspace,float64,log10, ones, vstack, arange
from numpy.linalg import norm, lstsq
from scipy.optimize import newton
import matplotlib.pyplot as plt
from time import process_time
import Test1



def Kepler(U, t): 

    x = U[0]; y = U[1]; dxdt = U[2]; dydt = U[3]
    d = ( x**2  +y**2 )**1.5

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 

def Euler( U, dt, t, F): 

   return U + dt * F( U, t ) 

def RK4( U, dt, t, F): 

     k1 = F( U, t)
     k2 = F( U + dt * k1/2, t + dt/2 )
     k3 = F( U + dt * k2/2, t + dt/2 )
     k4 = F( U + dt * k3,   t + dt   )
 
     return U + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6

def Crank_Nicolson(U, dt, t, F ): 

    def Residual_CN(X): 
         
         return  X - a - dt/2 *  F(X, t + dt)

    a = U  +  dt/2 * F( U, t)  
    return newton( Residual_CN, U )


dt = 0.01
t = arange(0, 200, dt)  
U0 = array( [1, 0, 0, 1 ] )
order = 2

print("Error Kepler orbit ") 
# Error1 = Test1.Error_Cauchy_Problem( t, Kepler,  Crank_Nicolson, order, U0 )

#plt.plot(t, Error1[:,0] )
plt.axis('equal')
plt.grid()
plt.show()


        
 
N = 2000
t = linspace(0, 10, N) 
U0 = array( [1, 0, 0, 1 ] )
m = 5

print("Order Euler ") 
# log_e1, log_n1 = Test1.Temporal_convergence_rate( t, Kepler, U0, Euler, m )

# log_e2, log_n2 = Test1.Temporal_convergence_rate( t, Kepler, U0, Crank_Nicolson, m )

log_e3, log_n3 = Test1.Temporal_convergence_rate( t, Kepler, U0, RK4, m )

print( "order =", order)
#plt.plot(log_n1, log_e1 )
plt.axis('equal')
plt.grid()
plt.show()



