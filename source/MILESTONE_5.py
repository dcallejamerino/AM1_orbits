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

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row
    z = U[2, :]  # Collect y values or values of the 3rd row

    return U


#------------------------------------------------------------------
# Orbits of N bodies 
#      U : state vector
#      r, v: position and velocity points to U     
#------------------------------------------------------------------    


def Init():

    #Function to define initial values
    #Definition of number of coordinates, bodies, speed, and initial position of each body

    Nc = 3 #number of coordinates: R3
    Nb = 3 #number of bodies
 
    Uo =  zeros(2*Nc*Nb)                    #Column vector with number of rows as needed
    Uord  = reshape(Uo,(Nb, Nc, 2))         #Pointer number #1
    r0 = reshape(Uord[:,:,0],(Nb, Nc))      #Pointer number #2
    v0 = reshape(Uord[:,:,1],(Nb, Nc))      #Pointer number #3
    
    #Cuerpo 1
    r0[0,:] = [0.5, -0.5, 0]                #initial position body 1
    v0[0,:] = [0.1, 0.1, 0.3]               #initial speed body 1
    #Cuerpo 2
    r0[1,:] = [0, 0, 0]                     #initial position body 2
    v0[1,:] = [-0.1, -0.1, 0.5]             #initial speed body 2
    #Cuerpo 3
    r0[2,:] = [-0.4, 0.5, 0]                #initial position body 3
    v0[2,:] = [-0.35, -0.3, 0.3]            #initial speed body 3
    #Cuerpo 4
    #r0[3,:] = [0, -1, 0]                   #initial position body 4
    #v0[3,:] = [0.5, 0, 0.05]               #initial speed body 4

    return Uo, Nc, Nb

# Definition of final time, number of divisions and initial conditions
tf = 2.3
N = 3900
t = linspace(0, tf, N+1)
Uo, Nc, Nb = Init()

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



def animate(num, data, line):
   line.set_data(data[0:2, :num])
   line.set_3d_properties(data[2, :num])
   return line

x = zeros([N+1])
y = zeros([N+1])
z = zeros([N+1])
for i in range(N):
    x[i] = r[i,0,0]
    y[i] = r[i,0,1]
    z[i] = r[i,0,2]

data = array([x, y, z])
fig = plt.figure()
ax = Axes3D(fig)

line, = plt.plot(data[0], data[1], data[2], lw=1, c='red')
line_ani = animation.FuncAnimation(fig, animate, frames=N, fargs=(data, line), interval=1, blit=False)

x2 = zeros([N+1])
y2 = zeros([N+1])
z2 = zeros([N+1])
for j in range(N):
    x2[j] = r[j,1,0]
    y2[j] = r[j,1,1]
    z2[j] = r[j,1,2]

data2 = array([x2, y2, z2])

line2, = plt.plot(data2[0], data2[1], data2[2], lw=1, c='blue')
line_ani2 = animation.FuncAnimation(fig, animate, frames=N, fargs=(data2, line2), interval=1, blit=False)

x3 = zeros([N+1])
y3 = zeros([N+1])
z3 = zeros([N+1])
for j in range(N):
    x3[j] = r[j,2,0]
    y3[j] = r[j,2,1]
    z3[j] = r[j,2,2]

data3 = array([x3, y3, z3])

line3, = plt.plot(data3[0], data3[1], data3[2], lw=1, c='green')
line_ani3 = animation.FuncAnimation(fig, animate, frames=N, fargs=(data3, line3), interval=1, blit=False)

#x4 = zeros([N+1])
#y4 = zeros([N+1])
#z4 = zeros([N+1])
#for j in range(N):
#    x4[j] = r[j,3,0]
#    y4[j] = r[j,3,1]
#    z4[j] = r[j,3,2]

#data4 = array([x4, y4, z4])

#line4, = plt.plot(data4[0], data4[1], data4[2], lw=1, c='purple')
#line_ani4 = animation.FuncAnimation(fig, animate, frames=N, fargs=(data4, line4), interval=1, blit=False)

plt.show()
