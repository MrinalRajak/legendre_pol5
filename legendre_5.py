
#legendre polynomial
#(5) (x**2-1)*P'(n,x) = n*(x*P(n,x)-P(n-1,x))

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=int(input("Enter the n: "))

def f(x):
    return legendre(n)(x)
LHS=(x**2-1)*derivative(f,x,order=15)
RHS=n*(x*(legendre(n)(x))-legendre(n-1)(x))
print("LHS: ",LHS)
print("RHS: ",RHS)
