
from numpy import           array, zeros, reshape, shape, linspace, concatenate, split, ceil, sqrt    
from numpy.linalg import    norm
from scipy.integrate import odeint, ode, solve_ivp
import matplotlib.pyplot as plt

from  numpy import array, zeros, reshape, float64
from time import process_time

def RK4 (U, t, dt, F): #CHEQUADO: ESTE ES MI RK4

     k1 = F( U, t)
     k2 = F( U + dt * k1/2, t + dt/2 )
     k3 = F( U + dt * k2/2, t + dt/2 )
     k4 = F( U + dt * k3,   t + dt   )
 
     return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6


# def Cauchy_problem( F, t, U0, Temporal_scheme): 


#  N, Nv=  len(t)-1, len(U0)
#  U = zeros( (N+1, Nv), dtype=float64) 

#  U[0,:] = U0
#  for n in range(N):

#      U[n+1,:] = Temporal_scheme( U[n, :], t[n+1] - t[n], t[n],  F ) 


#  return U

def Cauchy_problem(F, t, U0, temporal_scheme): #CHEQUADO: ESTE ES MI CAUCHY
    Nv = len(U0)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((N + 1,Nv), dtype=float64)
    U[0, :] = U0

    for i in range(N):
        U[i + 1,:] = temporal_scheme(U[i, :], t[i], t[i+1]-t[i], F)

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row
    z = U[2, :]  # Collect y values or values of the 3rd row

    return U


#-----------------------------------------------------------------
#  dvi/dt = - G m sum_j (ri- rj) / | ri -rj |**3, dridt = vi 
#----------------------------------------------------------------- 
def F_NBody(U, t, Nb, Nc): #CHEQUADO: ESTE ES MI NBODY
    F =  zeros(len(U))
    Us  = reshape(U,(Nb, Nc, 2))
    dUs = reshape(F,(Nb, Nc, 2))

    r = reshape(Us[:,:,0],(Nb, Nc))
    v = reshape(Us[:,:,1],(Nb, Nc))
    
    drdt = reshape(dUs[:,:,0], (Nb,Nc))
    dvdt = reshape(dUs[:,:,1], (Nb,Nc))
    
    dvdt[:,:] = 0
    
    for i in range(Nb):
        drdt[i,:] = v[i,:]
        for j in range(Nb):
            if j != i:
                dvdt[i,:] = dvdt[i,:] + (r[j,:]-r[i,:])/norm(r[j,:]-r[i,:])**3 
    
    return F

 
#------------------------------------------------------------------
# Orbits of N bodies 
#      U : state vector
#      r, v: position and velocity points to U     
#------------------------------------------------------------------    
def Integrate_NBP():  
    
   def F(U,t): 
       return F_NBody(U, t, Nb, Nc) 

   N =  1000    # time steps 
   Nb = 4      # bodies 
   Nc = 3      # coordinates 
   Nt = (N+1) * 2 * Nc * Nb

   t0 = 0; tf = 4 * 3.14 
   Time = linspace(t0, tf, N+1) # Time(0:N) 
 
   U0 = Initial_positions_and_velocities( Nc, Nb )
 
  #U = odeint(F_NBody, U0, Time)
   U = Cauchy_problem(F, Time, U0, RK4) 

   Us  = reshape( U, (N+1, Nb, Nc, 2) ) 
   r   = reshape( Us[:, :, :, 0], (N+1, Nb, Nc) ) 
   
   for i in range(Nb):
     plt.plot(  r[:, i, 0], r[:, i, 1] )
   plt.axis('equal')
   plt.grid()
   plt.show()
  
#------------------------------------------------------------
#  Initial codition: 6 degrees of freedom per body  
#------------------------------------------------------------
def Initial_positions_and_velocities( Nc, Nb ): 
 
    U0 =  zeros(2*Nc*Nb)
    U1  = reshape( U0, (Nb, Nc, 2) )  
    r0 = reshape( U1[:, :, 0], (Nb, Nc) )     # position and velocity 
    v0 = reshape( U1[:, :, 1], (Nb, Nc) )

    # body 1 
    r0[0,:] = [ 1, 0, 0]
    v0[0,:] = [ 0, 0.4, 0]

    # body 2 
    v0[1,:] = [ 0, -0.4, 0] 
    r0[1,:] = [ -1, 0, 0]

    # body 3 
    r0[2, :] = [ 0, 1, 0 ] 
    v0[2, :] = [ -0.4, 0., 0. ] 
         
    # body 4 
    r0[3, :] = [ 0, -1, 0 ] 
    v0[3, :] = [ 0.4, 0., 0. ]  

    return U0 

if __name__ == '__main__': 
     Integrate_NBP()  
