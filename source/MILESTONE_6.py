from numpy import array, linspace, zeros, around, float64, real, imag, transpose
import matplotlib.pyplot as plt
from random import random

from ODEs.Temporal_Schemes import Euler, CN, RK4, Inverse_Euler, LF
from ODEs.RK_Embedded import RKEmb
from Physic.Nbody_function import N_Body
from Physic.Resolution_3Body import CR3BP, Lpoints, Stability
from Stability.Stability_Regions import Stability_region


### MAIN INPUTS FOR THE CALCULATION ###
sel_LG = 5  # which Lagrange Point we desire to simulate in the last graphs of the script (LP5 by default)
orbitcalculation = 1 # will allow to calculate a longer or shorter orbit around a Lagrange Point (values between 1 and 10 presents good results at low computation times)


## CAUCHY ##
# Cauchy for Lagrange problem 

def Cauchy_problem_Lagrange(F, t, U0, temporal_scheme): # rows/columns inverted versus the standard cauchy
    Nv = len(U0)  # number of columns needed
    N = len(t) - 1  # number of rows needed
    U = zeros((N + 1,Nv), dtype=float64)
    U[0, :] = U0

    for i in range(N):
        U[i + 1,:] = temporal_scheme(U[i, :], t[i], t[i+1]-t[i], F)

    return U


##  Final time and number of divisions ## 

N = int(1e4)
t = linspace(0, orbitcalculation, N)
mu = 1.2151e-2 #Earth-Moon
#mu = 3.0039e-7 #Sun-Moon


##  Cauchy function that I call since it has more inputs than (U,t) ## 

def F(U,t):
   return CR3BP(U, mu)


##  Lagrage points starting from close points ## 

U0LP = array([[0.1, 0, 0, 0],[1.01, 0, 0, 0],[-0.1, 0, 0, 0],[0.8, 0.6, 0, 0],[0.8, -0.6, 0, 0]])
LagPoints = Lpoints(U0LP, 5, mu)

##  Print the calculated Lagrange points with labels in th command window ## 

for i, lag_point in enumerate(LagPoints):
    label = f"L{i + 1}"  # Adjust the index based on your preferred numbering (e.g., L1, L2, etc.)
    print(f"{label}: {lag_point}")


##  Generation of initial condicions close to a Lagrange point ## 

U0 = zeros(4)
U0[0:2] = LagPoints[sel_LG-1,:]
ran = 1e-4*random()
U0 = U0 + ran


## Integration of the circular restricted problem of the 3 Bodies thru a temporal scheme  ## 

temporal_scheme = CN
U  = Cauchy_problem_Lagrange(F, t, U0, temporal_scheme)


 ## Evaluation of the stability in Lagrange points ## 

for i in range(5):
    U0S = zeros(4)
    U0S[0:2] = LagPoints[i,:]
    eingvalues = Stability(U0S, mu)
    # Print Lagrange point index and corresponding stability evaluation
    print(f"LP {i+1} eingvalue: {around(eingvalues.real, 4)}")
    
    # Stability analysis
        #If Re(lambda_i)<0 -> Stable
        #If Re(lambda_i)>0 -> Unstable: L1, L2, L3
        #If Re(lambda_i)=0-> Marginally stable: L4 and L5

U0S = zeros(4)
U0S[0:2] = LagPoints[0,:]
eingvalues1 = Stability(U0S, mu)
U0S[0:2] = LagPoints[1,:]
eingvalues2 = Stability(U0S, mu)
U0S[0:2] = LagPoints[2,:]
eingvalues3 = Stability(U0S, mu)
U0S[0:2] = LagPoints[3,:]
eingvalues4 = Stability(U0S, mu)
U0S[0:2] = LagPoints[4,:]
eingvalues5 = Stability(U0S, mu)
 
# CN
(x1, y1, rho1) = Stability_region(CN,100,0.0005,-0.0005,0.0005,-0.0005)
plt.contour( x1, y1, transpose(rho1), linspace(0, 1, 11))
plt.scatter(real(eingvalues1*orbitcalculation/N), imag(eingvalues1*orbitcalculation/N), color='red',label='LP1: dt={}'.format(orbitcalculation/N))
plt.scatter(real(eingvalues2*orbitcalculation/N), imag(eingvalues2*orbitcalculation/N), color='blue',label='LP2: dt={}'.format(orbitcalculation/N))
plt.scatter(real(eingvalues3*orbitcalculation/N), imag(eingvalues3*orbitcalculation/N), color='orange',label='LP3: dt={}'.format(orbitcalculation/N))
plt.scatter(real(eingvalues4*orbitcalculation/N), imag(eingvalues4*orbitcalculation/N), color='yellow',label='LP4: dt={}'.format(orbitcalculation/N))
plt.scatter(real(eingvalues5*orbitcalculation/N), imag(eingvalues5*orbitcalculation/N), color='green',label='LP5: dt={}'.format(orbitcalculation/N))
plt.legend()
plt.xlabel('Re(w)')
plt.ylabel('Im(w)') 
plt.axis('equal')
plt.axvline(0, color='black', linestyle='--', linewidth=2)
plt.title('Regions of absolute stability of Lagrange points using CN')
plt.grid()
plt.show()



 ## Graphs  ## 
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
fig.suptitle("Orbit around L{} with CN".format(sel_LG))
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