from numpy import linspace, size, zeros, log10, float64, ones, vstack, array
from numpy.linalg import norm, lstsq
from ODEs.Temporal_Schemes import Euler, CN, RK4, Inverse_Euler

# CAUCHI for Richardson error without "x" and "y" as output ("x" and "y" needed for math theory plotting)
# ------------------------------------------------------------------------------- #
#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N+1)
    # dt: time step
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py

#RETURN:
    # U: matrix[Nv, N+1], Nv state values at N+1 time steps 
# ------------------------------------------------------------------------------- #

def Cauchy_problem_rich(F, t, Uo, temporal_scheme):
    Nv = len(Uo)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((Nv, N + 1), dtype=float64)
    U[:, 0] = Uo

    for i in range(N):
        U[:, i + 1] = temporal_scheme(U[:, i], t[i], t[i+1]-t[i], F)

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row

    return U


### Richardson error##
# ------------------------------------------------------------------------------- #
#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py

#RETURN:
    # E: matrix[Nv, N+1], Nv state values at N time steps 
# ------------------------------------------------------------------------------- #

def Richardson_error(F, t, Uo, temporal_scheme): 
   
    # Variable definition
    Nv = len(Uo)  # number of rows needed for E
    N = len(t)-1  # number of columns needed for E

    t1 = t
    t2 = zeros(2*N+1) 
    E = zeros([Nv, N+1],dtype=float64) 
    
    # Even loop
    for i in range(N+1):  
        t2[2*i]   = t1[i] 

    # Odd loop
    for i in range(N):  
        t2[2*i+1] = ( t1[i] + t1[i+1] )/2

    # Calculation of solutions for two different steps
    U1 = Cauchy_problem_rich(F, t1, Uo, temporal_scheme)
    U2 = Cauchy_problem_rich(F, t2, Uo, temporal_scheme)
    
    # Definition of the temporal scheme order
    if temporal_scheme == RK4:
        q = 4
    elif temporal_scheme == CN:
        q = 2
    else:
        q = 1
    
    # Error calculation

    for i in range(N+1):
        E[:, i] = (U2[:, 2*i] - U1[:, i]) / (1 - 1./(2**q))
    
    return E


### Convergence ratio ###
# ------------------------------------------------------------------------------- #
#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
    # p: is the number of points in the graph 

#RETURN:
    # Elog and Nlog
# ------------------------------------------------------------------------------- #

def Convergency(F, t, Uo, temporal_scheme, p):
    
    # Variable definition
    Elog = zeros(p)
    Nlog = zeros(p)
    N = len(t)-1
    t1 = t
    U1 = Cauchy_problem_rich(F, t1, Uo, temporal_scheme)
    
    # Definition of the temporal scheme order
    if temporal_scheme == RK4:
        q = 4
    elif temporal_scheme == CN:
        q = 2
    else:
        q = 1

    # Calculation of LogN and LogE
    for i in range(p): 
         N =  2 * N 
         t2 = array( zeros(N+1) )
         t2[0:N+1:2] =  t1
         t2[1:N:2] = ( t1[1:int(N/2)+1]  + t1[0:int(N/2)] )/ 2 
         U2 = Cauchy_problem_rich(F, t2, Uo, temporal_scheme)          
        
         E = norm( U2[:, N] - U1[:, int(N/2)] )  
         Elog[i] = log10( E ) - log10( 1 - 1/2**q)  
         Nlog[i] = log10( N )
         t1 = t2;  
         U1 = U2;   
  
    # print(Nlog, Elog)

    return [Elog, Nlog]

         
