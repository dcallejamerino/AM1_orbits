from numpy import array, linspace, zeros, around, float64, real, imag, transpose
import matplotlib.pyplot as plt
from random import random

import Temporal_Schemes, RK_Embedded, Resolution_3Body, Stability_Regions

### CAUCHY ###
# Cauchy for Lagrange problem 

def Cauchy_problem_Lagrange(F, t, U0, temporal_scheme): # rows/columns inverted versus the standard cauchy
    Nv = len(U0)  # number of columns needed
    N = len(t) - 1  # number of rows needed
    U = zeros((N + 1,Nv), dtype=float64)
    U[0, :] = U0

    for i in range(N):
        U[i + 1,:] = temporal_scheme(U[i, :], t[i], t[i+1]-t[i], F)

    return U


# Final time and number of divisions

N = int(1e4)
t = linspace(0, 1, N)
mu = 1.2151e-2 #Earth-Moon
#mu = 3.0039e-7 #Sun-Moon


# Cauchy function that I call since it has more inputs than (U,t)
def F(U,t):
   return Resolution_3Body.CR3BP(U, mu)


# Lagrage points starting from close points
U0LP = array([[0.1, 0, 0, 0],[1.01, 0, 0, 0],[-0.1, 0, 0, 0],[0.8, 0.6, 0, 0],[0.8, -0.6, 0, 0]])
LagPoints = Resolution_3Body.Lpoints(U0LP, 5, mu)

# Print the calculated Lagrange points with labels
for i, lag_point in enumerate(LagPoints):
    label = f"L{i + 1}"  # Adjust the index based on your preferred numbering (e.g., L1, L2, etc.)
    print(f"{label}: {lag_point}")


# Generation of initial condicions close to a Lagrange point
sel_LG = 5

U0 = zeros(4)
U0[0:2] = LagPoints[sel_LG-1,:]
ran = 1e-4*random()
U0 = U0 + ran


#Integration of the circular restricted problem of the 3 Bodies thru a temporal scheme
temporal_scheme = Temporal_Schemes.CN
U  = Cauchy_problem_Lagrange(F, t, U0, temporal_scheme)


#Evaluation of the stability in Lagrange points
for i in range(5):
    U0S = zeros(4)
    U0S[0:2] = LagPoints[i,:]
    eingvalues = Resolution_3Body.Stability(U0S, mu)
    # Print Lagrange point index and corresponding stability evaluation
    print(f"LP {i+1} eingvalue: {around(eingvalues.real, 4)}")
    
    # Stability analysis
        #If Re(lambda_i)<0 -> Stable
        #If Re(lambda_i)>0 -> Unstable: L1, L2, L3
        #If Re(lambda_i)=0-> Marginally stable: L4 and L5

U0S = zeros(4)
U0S[0:2] = LagPoints[0,:]
eingvalues1 = Resolution_3Body.Stability(U0S, mu)
U0S[0:2] = LagPoints[1,:]
eingvalues2 = Resolution_3Body.Stability(U0S, mu)
U0S[0:2] = LagPoints[2,:]
eingvalues3 = Resolution_3Body.Stability(U0S, mu)
U0S[0:2] = LagPoints[3,:]
eingvalues4 = Resolution_3Body.Stability(U0S, mu)
U0S[0:2] = LagPoints[4,:]
eingvalues5 = Resolution_3Body.Stability(U0S, mu)
 
# CN
(x1, y1, rho1) = Stability_Regions.Stability_region(Temporal_Schemes.CN,100,0.0005,-0.0005,0.0005,-0.0005)
plt.contour( x1, y1, transpose(rho1), linspace(0, 1, 11))
plt.scatter(real(eingvalues1*1/N), imag(eingvalues1*1/N), color='red',label='LP1: dt=1/N')
plt.scatter(real(eingvalues2*1/N), imag(eingvalues2*1/N), color='blue',label='LP2: dt=1/N')
plt.scatter(real(eingvalues3*1/N), imag(eingvalues3*1/N), color='orange',label='LP3: dt=1/N')
plt.scatter(real(eingvalues4*1/N), imag(eingvalues4*1/N), color='yellow',label='LP4: dt=1/N')
plt.scatter(real(eingvalues5*1/N), imag(eingvalues5*1/N), color='green',label='LP5: dt=1/N')
plt.legend()
plt.xlabel('Re(w)')
plt.ylabel('Im(w)') 
plt.axis('equal')
plt.axvline(0, color='black', linestyle='--', linewidth=2)
plt.title('Regions of absolute stability of Lagrange points using CN')
plt.grid()
plt.show()



#Graphs
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(U[:,0], U[:,1],'-',color = "r")
ax1.plot(-mu, 0, 'o', color = "g")
ax1.plot(1-mu, 0, 'o', color = "b")
for i in range(5):
    ax1.plot(LagPoints[i,0], LagPoints[i,1] , 'o', color = "k")
ax2.plot(U[:,0], U[:,1],'-',color = "r")
ax2.plot(LagPoints[sel_LG-1,0], LagPoints[sel_LG-1,1] , 'o', color = "k")
ax1.set_title("Orbital view")
ax2.set_title("Close-up")
fig.suptitle("Orbit around L2 with CN")
for ax in fig.get_axes():
    ax.set(xlabel='x', ylabel='y')
    ax.grid()

plt.show()


# Lagrange points are positions in space where objects sent there tend to stay put. 
# At Lagrange points, the gravitational pull of two large masses precisely equals the centripetal force required for a small object to move with them. 
# These points in space can be used by spacecraft to reduce fuel consumption needed to remain in position.
# Of the five Lagrange points, three are unstable and two are stable. 
# The unstable Lagrange points - labeled L1, L2 and L3 - lie along the line connecting the two large masses. 
# The stable Lagrange points - labeled L4 and L5 - form the apex of two equilateral triangles that have the large masses at their vertices. 
# L4 leads the orbit of earth and L5 follows.