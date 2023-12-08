#Temporal Schemes

from numpy import array, zeros
from scipy.optimize import newton
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------- #
#INPUTS:
    # The function F(U, t) of the Cauchy problem is input argument: dU/dt= F(U,t) 
    # U (t) is the state vector
    # t: tn
    # dt: time step

#RETURN:
    # U state vector at tn + dt 

#OTHERS:
    # U(to) = Uo are the initial conditions for t=0
# ------------------------------------------------------------------------------- #

# 1. Write a function called EULER to integrate one step 

def Euler (U, t, dt, F): 
    
    return  U + dt * F(U,t)


# 2. Write a function called CN to integrate one step

def CN (U, t, dt, F): 

    def Residual_CN(X): 
         
         return  X - U  -  dt/2 * F(U, t)  - dt/2 *  F(X, t+dt)
         
    return newton( Residual_CN, U )


# 3. Write a function called RK4 to integrate one step

def RK4 (U, t, dt, F): 

     k1 = F( U, t)
     k2 = F( U + dt * k1/2, t + dt/2 )
     k3 = F( U + dt * k2/2, t + dt/2 )
     k4 = F( U + dt * k3,   t + dt   )
 
     return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6


# 4.Write a function called Inverse_Euler to integrate one step

def Inverse_Euler (U, t, dt, F): 

    def Residual_Eu(X): 
          return X - U - dt * F(X, t+dt)

    return newton( Residual_Eu, U )

# def LF(U2, U1, t, dt, F):

#     return U1 + 2*dt*F(U2,t)

