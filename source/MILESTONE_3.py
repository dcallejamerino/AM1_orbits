# MILESTONE 3

from numpy import array, zeros, float64, arange
from scipy.optimize import newton
import numpy as np
import matplotlib.pyplot as plt
import Temporal_Schemes, Physics, Cauchy_problem, Richardson

# 1. Write a function to evaluate errors by means of Richardson: Refer to Richardson.py

# 2.Numerical error of different temporal schemes

# Richardson error
#INPUTS:
    # F(U,t) : Function dU/dt = F(U,t) -> from Physics.py
    # t : time partition t (vector of length N)
    # dt: time step (not used)
    # Uo : initial condition at t=0
    # Temporal_scheme is any of the numerical methods used to resolve the problem -> from Temporal_schemes.py

#RETURN:
    # E: matrix[Nv, N+1], Nv state values at N+1 time steps 

# Euler
F = Physics.Kepler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array( [1,0,0,1] ) 
temporal_scheme = Temporal_Schemes.Euler

E_EULER = Richardson.Richardson_error(F, t, dt, Uo, temporal_scheme)
plt.plot(t, E_EULER[0,:],label='EULER')

# CN
F = Physics.Kepler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array( [1,0,0,1] ) 
temporal_scheme = Temporal_Schemes.CN

E_CN = Richardson.Richardson_error(F, t, dt, Uo, temporal_scheme)
plt.plot(t, E_CN[0,:],label='CN')

# RK4
F = Physics.Kepler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array( [1,0,0,1] ) 
temporal_scheme = Temporal_Schemes.RK4

E_RK4 = Richardson.Richardson_error(F, t, dt, Uo, temporal_scheme)
plt.plot(t, E_RK4[0,:],label='RK4')

# # Inverse Euler
# F = Physics.Kepler
# dt = 0.1
# t = np.linspace(0, 20, 21) 
# Uo = array( [1,0,0,1] ) 
# temporal_scheme = Temporal_Schemes.Inverse_Euler

# E_IE = Richardson.Richardson_error(F, t, dt, Uo, temporal_scheme)
# plt.plot(t, E_IE[0,:],label='Inverse_Euler')

#Graph
plt.xlabel('t')
plt.ylabel('ERROR') 
plt.legend()
plt.title('Numerical error of different schemes solving Kepler')
plt.show()


# 3. Write a function to evaluate the convergence rate of different temporal schemes: Refer to Richardson.py

# 4. Convergence rate of the different methods with the time step

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

# Euler
F = Physics.Kepler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array( [1,0,0,1] ) 
temporal_scheme = Temporal_Schemes.Euler
p=5

[log_E_EULER, log_N_EULER] = Richardson.Convergency(F, t, dt, Uo, temporal_scheme,p)
plt.plot(log_N_EULER, log_E_EULER,label='EULER')

# CN
F = Physics.Kepler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array( [1,0,0,1] ) 
temporal_scheme = Temporal_Schemes.CN
p=5

[log_E_CN, log_N_CN] = Richardson.Convergency(F, t, dt, Uo, temporal_scheme,p)
plt.plot(log_N_CN, log_E_CN,label='CN')

# RK4
F = Physics.Kepler
dt = 0.01
t = arange(0, 200, dt)  
Uo = array( [1,0,0,1] ) 
temporal_scheme = Temporal_Schemes.RK4
p=5

[log_E_RK4, log_N_RK4] = Richardson.Convergency(F, t, dt, Uo, temporal_scheme,p)
plt.plot(log_N_RK4, log_E_RK4,label='RK4')

#Graph
plt.xlabel('log_N')
plt.ylabel('log_E') 
plt.legend()
plt.title('Convergence rate of the different methods solving Kepler')
plt.show()