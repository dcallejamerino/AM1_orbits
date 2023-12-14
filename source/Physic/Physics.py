# PHYSICS

from numpy import array, zeros,cos


def Kepler(U, t): # Initial value of U: U = array( [1,0,0,1] ) 

    x = U[0]; y = U[1]; dxdt = U[2]; dydt = U[3]
    d = ( x**2  +y**2 )**1.5

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 

def Oscillator(U, t): # Initial value of U: U = array( [1,0] ) 

    x = U[0]; dxdt = U[1]; 

    return  array( [ dxdt, -x ] ) 

def Clase(U, t): 

    x = U[0]
    y = U[1]
    
    return  array ( [3*x-2*y, 2*x-2*y] )

def Brusellator(U, t): 

    x = U[0]
    y = U[1]
    
    return  array ( [1-4*x+y*x**2, 3*x-y*x**2] )

def Duffing0(U, t): #Duffing con k=1, B=1

    x = U[0]
    y = U[1]
    
    return  array ( [y, -x**3-y+cos(t)] )

def Duffing1(U, t): #Duffing con k=0.05, B=1 (a mayor k mas caotico)

    x = U[0]
    y = U[1]
    
    return  array ( [y, -x**3-0.05*y+cos(t)] )

def Duffing2(U, t): #Duffing con k=0.0001, B=1

    x = U[0]
    y = U[1]
    
    return  array ( [y, -x**3-0.001*y+cos(t)] )

def VanderPol(U, t): #Van der Pol con wo=1, u=0.2

    x = U[0]
    y = U[1]
    
    return  array ( [y, -1*x-0.2*(x**2-1)*y] )

def Rayleigh(U, t): #Rayleigh fo=0.6 (periodico), f0=0.7 (ciclo doble: se repite cada 2 vueltas), fo=0.75 (ciclo cuadruple: se repite cada 4 vueltas)

    x = U[0]
    y = U[1]
    
    return  array ( [y, x-x**3-y+0.6*cos(t)] )

def Lorentz(U, t): #Lorentz para b=8/3, r=28, s=10

    x = U[0]
    y = U[1]
    z = U[2]
    
    return  array ( [-10*x+10*y, 28*x-x*z-y, -8/3*z+x*y] )

def Rossler(U, t): #Rossler para b=2, c=4, a=0.398 y Rossler para b=0.4, c=8.5, a=0.17

    x = U[0]
    y = U[1]
    z = U[2]
    
    return  array ( [-y-z, 0.17*y+x, 0.4+z*x-z*8.5] )