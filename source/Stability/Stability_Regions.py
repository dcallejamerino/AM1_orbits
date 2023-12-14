from numpy import array, abs, linspace, zeros,float64, max, transpose  
from scipy.optimize import newton
import matplotlib.pyplot as plt


### Stability Regions ###
# ------------------------------------------------------------------------------- #
#INPUTS:
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
    # N: normally 100
    # x0,xf,y0,yf: Limit values of the plane

#RETURN:
    # x, y, rho
# ------------------------------------------------------------------------------- #


def Stability_region(scheme,N,x0,xf,y0,yf): 

    x, y = linspace(x0, xf, N), linspace(y0, yf, N)
    rho = zeros ((N, N), dtype=float64)
    
    for i  in range (N):
        for j in range (N):
             w = complex(x[i], y[j])
             r = scheme(1.,0.,1., lambda u, t:w*u)
             rho[i,j] =  abs(r)

    return (x, y, rho) 



# def test_stability_regions():

#     schemes = [Temporal_Schemes.Euler,Temporal_Schemes.RK4, Temporal_Schemes.CN, Temporal_Schemes.Inverse_Euler]

#     for scheme in schemes:
#         (x, y, rho) = Stability_region(scheme,100,-4,4,-4,4 )
#         plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
#         plt.axis('equal')
#         plt.grid()
#         plt.show()
#     print (x, y, rho)
# test_stability_regions()