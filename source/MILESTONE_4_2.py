# MILESTONE 4

from numpy import array, zeros, float64, arange, transpose, linspace, linalg, real, imag
from scipy.optimize import newton
import matplotlib.pyplot as plt
import Temporal_Schemes, Physics, Cauchy_problem, Stability_Regions

# 3. Explain the numerical results based on regions of absolute stability (based on the plots of point 2)

# Linear oscillator matrix A a
A = array([[0, 1], [-1, 0]])
Eigenvalues = linalg.eigvals(A)
print ("Eigenvalues A", Eigenvalues)
dt1 = 1
dt2 = 0.1
dt3 = 0.01

#Numerical stability for lambda in the border of the region of absolute stability of the numerical method: norm(r)=1. Analysis for linear oscillator
# Euler-> lambda x dt outside of the region of absolute stability: numerically unstable for any dt
# Inverse Euler-> lambda x dt inside of the region of absolute stability: numerically unstable for any dt (dissipation of energy)
# CN-> lambda x dt inside of the region of absolute stability: numerically stable for any dt
# RK4-> lambda x dt inside of the region of absolute stability: numerically stable. But some dt can make the system numerically unstable



# 2. Regions of absolute stability of the above methods.

### Stability Regions ###
# ------------------------------------------------------------------------------- #
#INPUTS:
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
    # N: normally 100
    # x0,xf,y0,yf: Limit values of the plane

#RETURN:
    # x, y, rho
# ------------------------------------------------------------------------------- #

# Euler
(x1, y1, rho1) = Stability_Regions.Stability_region(Temporal_Schemes.Euler,100,-2.5,0.5,-1.5,1.5 )
plt.contour( x1, y1, transpose(rho1), linspace(0, 1, 11))
plt.scatter(real(Eigenvalues*dt1), imag(Eigenvalues*dt1), color='red',label='dt=1')
plt.scatter(real(Eigenvalues*dt2), imag(Eigenvalues*dt2), color='orange',label='dt=0.1')
plt.scatter(real(Eigenvalues*dt3), imag(Eigenvalues*dt3), color='blue',label='dt=0.01')
plt.legend()
plt.xlabel('Re(w)')
plt.ylabel('Im(w)') 
plt.axis('equal')
plt.axvline(0, color='black', linestyle='--', linewidth=2)
plt.title('Regions of absolute stability Euler')
plt.grid()
plt.show()

# Inverse_Euler
(x2, y2, rho2) = Stability_Regions.Stability_region(Temporal_Schemes.Inverse_Euler,100,10,-10,10,-10)
plt.contour( x2, y2, transpose(rho2), linspace(0, 1, 11))
plt.scatter(real(Eigenvalues*dt1), imag(Eigenvalues*dt1), color='red',label='dt=1')
plt.scatter(real(Eigenvalues*dt2), imag(Eigenvalues*dt2), color='orange',label='dt=0.1')
plt.scatter(real(Eigenvalues*dt3), imag(Eigenvalues*dt3), color='blue',label='dt=0.01')
plt.legend()
plt.xlabel('Re(w)')
plt.ylabel('Im(w)') 
plt.axis('equal')
plt.axvline(0, color='black', linestyle='--', linewidth=2)
plt.title('Regions of absolute stability Inverse_Euler')
plt.grid()
plt.show()

# CN
(x3, y3, rho3) = Stability_Regions.Stability_region(Temporal_Schemes.CN,100,2,-5,8,-8)
plt.contour( x3, y3, transpose(rho3), linspace(0, 1, 11))
plt.scatter(real(Eigenvalues*dt1), imag(Eigenvalues*dt1), color='red',label='dt=1')
plt.scatter(real(Eigenvalues*dt2), imag(Eigenvalues*dt2), color='orange',label='dt=0.1')
plt.scatter(real(Eigenvalues*dt3), imag(Eigenvalues*dt3), color='blue',label='dt=0.01')
plt.legend()
plt.xlabel('Re(w)')
plt.ylabel('Im(w)') 
plt.axis('equal')
plt.axvline(0, color='black', linestyle='--', linewidth=2)
plt.title('Regions of absolute stability CN')
plt.grid()
plt.show()

# RK4
(x4, y4, rho4) = Stability_Regions.Stability_region(Temporal_Schemes.RK4,100,2,-4,4,-4)
plt.contour( x4, y4, transpose(rho4), linspace(0, 1, 11))
plt.scatter(real(Eigenvalues*dt1), imag(Eigenvalues*dt1), color='red',label='dt=1')
plt.scatter(real(Eigenvalues*dt2), imag(Eigenvalues*dt2), color='orange',label='dt=0.1')
plt.scatter(real(Eigenvalues*dt3), imag(Eigenvalues*dt3), color='blue',label='dt=0.01')
plt.legend()
plt.xlabel('Re(w)')
plt.ylabel('Im(w)') 
plt.axis('equal')
plt.axvline(0, color='black', linestyle='--', linewidth=2)
plt.title('Regions of absolute stability RK4')
plt.grid()
plt.show()
