# MILESTONE 2 

from numpy import array, zeros
from scipy.optimize import newton
import matplotlib.pyplot as plt

# The function F(U, t) of the Cauchy problem is input argument 
# dU/dt= F(U,t)
# U(to) = Uo

Uo = array( [1,0,0,1] ) # Initial value of U
to = 0                  # Initial time
dt = 0.001                # Time step size


# 1. Write a function called EULER to integrate one step

def Euler(Uo, dt, to, F): 
   
    U1 = Uo + dt * F( Uo, to)
    t1 = to + dt
    
    return  U1, t1


# 2. Write a function called CN to integrate one step

def CN (Uo, dt, to, F): 

    def Residual_CN(X): 
         
         return  X - a - dt/2 *  F(X, to + dt)

    a = U1  +  dt/2 * F(Uo, to)
    t1 = to + dt
    
    return newton( Residual_CN, U1 ), t1


# 3. Write a function called RK4 to integrate one step

def RK4(Uo, dt, to, F ): 

     k1 = F( Uo, to)
     k2 = F( Uo + dt * k1/2, to + dt/2 )
     k3 = F( Uo + dt * k2/2, to + dt/2 )
     k4 = F( Uo + dt * k3,   to + dt   )
 
     U1 = Uo + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6
     t1 = to + dt

     return  U1, t1


# 4.Write a function called Inverse_Euler to integrate one step

def Inverse_Euler(Uo, dt, to, F): 

    def Residual(X): 
          return X - U1 - dt * F(X, to)

    return newton(func = Residual, x0 = U1 ) , t1


# 5. Write a function to integrate a Cauchy problem. Temporal scheme, initial condition and the function F(U, t) of the Cauchy problem should be input arguments.


# 6. Write a function to express the force of the Kepler movement

def Kepler(Uo, t): 

    x = Uo[0]; y = Uo[1]; dxdt = Uo[2]; dydt = Uo[3]
    d = ( x**2  +y**2 )**1.5

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 


# 7. Integrate a Kepler with these latter schemes and explain the results

# Perform one step of Euler method & print
U1, t1 = Euler(Uo, dt, to, Kepler)
print(f"For Euler at t={t1}, U(t) is approximately {U1}")


# Perform one step of CN method & print
U1, t1 = CN(Uo, dt, to, Kepler)
print(f"For CN at t={t1}, U(t) is approximately {U1}")


# Perform one step of RK4 method & print
U1, t1 = RK4(Uo, dt, to, Kepler)
print(f"For RK4 at t={t1}, U(t) is approximately {U1}")


# Perform one step of Inverse Euler method & print
U1, t1 = Inverse_Euler(Uo, dt, to, Kepler)
print(f"For Inverse Euler at t={t1}, U(t) is approximately {U1}")

# 8. Increase and decrease the time step and explained the results
# Smaller dt shows a closer value of U1 vs U0 and more similarity between methods, while big dt shows less accuracy on implicit methods