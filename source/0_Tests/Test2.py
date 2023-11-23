# Prototype to integrate a Kepler orbit 
from  numpy import array, zeros, reshape, float64
from time import process_time

# def Cauchy_problem( F, t, U0, Temporal_scheme): 


#  start = process_time()
#  N, Nv=  len(t)-1, len(U0)
#  U = zeros( (N+1, Nv), dtype=float64) 

#  U[0,:] = U0
#  for n in range(N):

#      U[n+1,:] = Temporal_scheme( U[n, :], t[n+1] - t[n], t[n],  F ) 

#  finish = process_time()
#  print("Cauchy_Problem, CPU Time=",finish-start," seconds.") 
#  return U

def Cauchy_problem(F, t, U0, Temporal_scheme):
    Nv = len(U0) 
    N = len(t) - 1  
    U = zeros((N+1, Nv), dtype=float64)
    U[0, :] = U0

    for i in range(N):
        U[i + 1, :] = Temporal_scheme(U[i, :], t[i+1]-t[i],t[i], F)



    return U