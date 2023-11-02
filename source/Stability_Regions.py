from numpy import array, abs, linspace, zeros,float64, max, transpose  
from scipy.optimize import newton
import matplotlib.pyplot as plt
import Temporal_Schemes, Physics

# def Euler(U, dt, t, F): 

#     return U + dt * F(U, t)

def Euler (U, t, dt, F): 
    
    return  U + dt * F(U,t)

def RK4 (U, t, dt, F): 

     k1 = F( U, t)
     k2 = F( U + dt * k1/2, t + dt/2 )
     k3 = F( U + dt * k2/2, t + dt/2 )
     k4 = F( U + dt * k3,   t + dt   )
 
     return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6


def Stability_region(scheme,N,x0,xf,y0,yf): 

    x, y = linspace(x0, xf, N), linspace(y0, yf, N)
    rho = zeros ((N, N), dtype=float64)
    
    for i  in range (N):
        for j in range (N):
             w = complex(x[i], y[j])
             r = scheme(1.,0.,1., lambda u, t:w*u)
             rho[i,j] =  abs(r)

    return (x, y, rho) 


# (x, y, rho) = Stability_region(Euler,100,-4,4,-4,4)
# plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
# plt.axis('equal')
# plt.grid()
# plt.show()



def test_stability_regions():

    schemes = [Temporal_Schemes.Euler,Temporal_Schemes.RK4, Temporal_Schemes.CN, Temporal_Schemes.Inverse_Euler]

    for scheme in schemes:
        (x, y, rho) = Stability_region(scheme,100,-4,4,-4,4 )
        plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
        plt.axis('equal')
        plt.grid()
        plt.show()

test_stability_regions()