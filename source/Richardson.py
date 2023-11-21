from numpy import linspace, size, zeros, log10, float64
from numpy.linalg import norm
import numpy as np
import Temporal_Schemes, Cauchy_problem

# Cauchi for Richardson error without x and y as output (needed for math theory plotting)

def Cauchy_problem_rich(F, t, dt, Uo, temporal_scheme):
    Nv = len(Uo)  # number of rows needed
    N = len(t) - 1  # number of columns needed
    U = zeros((Nv, N + 1), dtype=float64)
    U[:, 0] = Uo

    for i in range(N):
        U[:, i + 1] = temporal_scheme(U[:, i], t[i], dt, F)

    x = U[0, :]  # Collect x values or values of the 1st row
    y = U[1, :]  # Collect y values or values of the 2nd row

    return U

# Richardson error
#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N)
    # dt: time step (not used)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py

#RETURN:
    # E: matrix[Nv, N+1], Nv state values at N time steps 

def Richardson_error(F, t, dt, Uo, temporal_scheme): 
    
    Nv = len(Uo)  # number of rows needed for E
    N = len(t) - 1  # number of columns needed for E

    E = np.zeros([Nv, N+1]) #  doubts if it is E = np.zeros([Nv, N+1])

    t1 = t
    t2 = np.linspace(0, t[N-1], 2*N) # Assuming you want to create a time vector from 0 to t[N-1]


    # Calculation of solutions for two different steps
    U1 = Cauchy_problem_rich(F, t1, dt, Uo, temporal_scheme)
    U2 = Cauchy_problem_rich(F, t2, dt, Uo, temporal_scheme)
    
    # Definition of the temporal scheme order
    if temporal_scheme == Temporal_Schemes.RK4:
        q = 4
    elif temporal_scheme == Temporal_Schemes.CN:
        q = 2
    else:
        q = 1
    
    # Error calculation

    for i in range(N):
        E[:, i] = (U2[:, 2*i] - U1[:, i]) / (1 - 1/(2**q))

    return E



 # Convergence ratio
#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N)
    # dt: time step (not used)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py
    # p: is the number of points in the graph 

#RETURN:
    # Elog and Nlog

# def Convergency(F, t, dt, Uo, temporal_scheme, p):

#     #First solution with N divisions
#     N = len(t) # doubts if it is N = len(t)-1
#     tf = t[N-1]
#     U  = Cauchy_problem_rich(F, t, dt, Uo, temporal_scheme)

#     #Inizializing the vectors
#     E = zeros(p)
#     Elog = zeros(p)
#     Nlog = zeros(p)
#     N = 2*N
    

#     for i in range(0,p):

#         #Solution with half step
#         t2 = linspace(0, tf, (2**i)*N)
#         U2N = Cauchy_problem_rich(F, t2, dt, Uo, temporal_scheme)

#         #Convergence ratio and logarithm
#         E[i] = norm((U2N[:,int((2**i)*N-1)] - U[:,int((2**i)*N/2-1)]))
#         Elog[i] = log10(E[i])
#         Nlog[i] = log10((2**i)*N)

#         U = U2N
#         print(i)

#     return [Elog, Nlog]

def Convergency(F, t, dt, Uo, temporal_scheme, p):
    tf = t[-1]  # Use the last element of the time vector

    E = np.zeros(p)
    Elog = np.zeros(p)
    Nlog = np.zeros(p)

    U = Cauchy_problem_rich(F, t, dt, Uo, temporal_scheme)

    for i in range(p):
        t2 = linspace(0, tf, int((2**i)*len(t)))  # Use int() to ensure a valid array size
        U2N = Cauchy_problem_rich(F, t2, dt, Uo, temporal_scheme)

        E[i] = norm(U2N[:, -1] - U[:, int(len(t2)/2 - 1)])
        Elog[i] = log10(E[i])
        Nlog[i] = log10((2**i)*len(t))

        U = U2N
        print(i)

    return [Elog, Nlog]

