# Differential Equations

from numpy import array, zeros

# Write a function to express the force of the Kepler movement (State vector 4 rows & 1 column)
# Initial value of U: U = array( [1,0,0,1] ) 

def Kepler(U, t): 

    x = U[0]; y = U[1]; dxdt = U[2]; dydt = U[3]
    d = ( x**2  +y**2 )**1.5

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 


# Write a function to express an harmonic oscillator (State vector 2 rows & 1 column)
# Initial value of U: U = array( [1,0] ) 

def Oscillator(U, t): 

    x = U[0]; dxdt = U[1]; 

    return  array( [ dxdt, -x ] ) 


def Clase(U, t): 

    x = U[0]
    y = U[1]
    
    return  array ( [3*x-2*y, 2*x-2*y] )


