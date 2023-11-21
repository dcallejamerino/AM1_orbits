# Differential Equations

from numpy import array, zeros,cos

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

def Clase2(U, t): 

    x = U[0]
    y = U[1]
    
    return  array ( [1-4*x+y*x**2, 3*x-y*x**2] )

def Clase3(U, t): #Duffing con k=1, B=1

    x = U[0]
    y = U[1]
    
    return  array ( [y, -x**3-y+cos(t)] )

def Clase4(U, t): #Duffing con k=0.05, B=1 (a mayor k mas caotico)

    x = U[0]
    y = U[1]
    
    return  array ( [y, -x**3-0.05*y+cos(t)] )

def Clase5(U, t): #Duffing con k=0.0001, B=1

    x = U[0]
    y = U[1]
    
    return  array ( [y, -x**3-0.001*y+cos(t)] )

def Clase6(U, t): #Van der Pol con wo=1, u=0.2

    x = U[0]
    y = U[1]
    
    return  array ( [y, -1*x-0.2*(x**2-1)*y] )

def Clase7(U, t): #Rayleigh fo=0.6 (periodico), f0=0.7 (ciclo doble: se repite cada 2 vueltas), fo=0.75 (ciclo cuadruple: se repite cada 4 vueltas)

    x = U[0]
    y = U[1]
    
    return  array ( [y, x-x**3-y+0.6*cos(t)] )

def Clase8(U, t): #Lorentz para b=8/3, r=28, s=10

    x = U[0]
    y = U[1]
    z = U[2]
    
    return  array ( [-10*x+10*y, 28*x-x*z-y, -8/3*z+x*y] )

def Clase9(U, t): #Rossler para b=2, c=4, a=0.398 y Rossler para b=0.4, c=8.5, a=0.17

    x = U[0]
    y = U[1]
    z = U[2]
    
    return  array ( [-y-z, 0.17*y+x, 0.4+z*x-z*8.5] )