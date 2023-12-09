from numpy import array, linspace, reshape, zeros, sqrt, arange, float64

import Temporal_Schemes, Nbody_function

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

### CAUCHY ###
# Cauchy for N-body problem (we have more inputs than U and t)

def Cauchy_problem_NBODY(F, t, Uo, temporal_scheme): # rows/columns inverted versus the standard cauchy
    Nv = len(Uo)  # number of columns needed
    N = len(t) - 1  # number of rows needed
    U = zeros((N + 1,Nv), dtype=float64)
    U[0, :] = Uo

    for i in range(N):
        U[i + 1,:] = temporal_scheme(U[i, :], t[i], t[i+1]-t[i], F)

    return U


#------------------------------------------------------------------
# Orbits of N bodies 
#      U : state vector
#      r, v: position and velocity points to U     
#------------------------------------------------------------------    

Nb = 4      # bodies 
Nc = 3      # coordinates 


def Init(Nc, Nb):

    #Function to define initial values
    #Definition of number of coordinates, bodies, speed, and initial position of each body

    Uo =  zeros(2*Nc*Nb)                  #Column vector with number of rows as needed
    U1  = reshape(Uo,(Nb, Nc, 2))         #Pointer number #1
    r0 = reshape(U1[:,:,0],(Nb, Nc))      #Pointer number #2
    v0 = reshape(U1[:,:,1],(Nb, Nc))      #Pointer number #3
    
    # body 1 
    r0[0,:] = [2, 0, 0]                #initial position body 1
    v0[0,:] = [0, 0.8, 0]              #initial speed body 1
    #Body 2
    r0[1,:] = [-2, 0, 0]                #initial position body 2
    v0[1,:] = [ 0, -0.8, 0]             #initial speed body 2
    #Body 3
    r0[2,:] = [0, 2, 0 ]                #initial position body 3
    v0[2,:] = [-0.8, 0., 0. ]           #initial speed body 3
    #Body 4
    r0[3,:] = [0, -2, 0]                 #initial position body 4
    v0[3,:] = [0.8, 0., 0.]              #initial speed body 4
    

    return Uo 


# Definition of final time, number of divisions and initial conditions

N =  1000                   # time steps 
tf = 16 * 3.14               # final time 
t = linspace(0, tf, N+1)    # Time(0:N)
Uo = Init( Nc, Nb )

def F(U, t):
   return Nbody_function.N_Body(U, t, Nb, Nc)


temporal_scheme = Temporal_Schemes.RK4
U  = Cauchy_problem_NBODY(F, t, Uo, temporal_scheme)



#Graph 3D
r   = reshape(U,(N+1, Nb, Nc, 2))[:,:,:,0]
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
col = ["blue","red","green","purple","yellow","orange","black"]
for i in range(Nb):
    ax1.plot_wireframe(r[:,i,0].reshape((-1, 1)), r[:,i,1].reshape((-1, 1)), r[:,i,2].reshape((-1, 1)), color = col[i])
plt.title("N-body problem")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
plt.grid()
plt.show()

#Graph 2D
for i in range(Nb):
   plt.plot(r[:, i, 0], r[:, i, 1], color = col[i])
plt.axis('equal')
plt.title("N-body problem X-Y Plane")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


# Different initial conditions can make the system to collapse. Higher initial speeds requires higher tf for a full orbit. Changed the IC to multiples of the originals to see how the system behave