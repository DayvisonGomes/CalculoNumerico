import math
import numpy as np
from numpy import *
from sympy import *

def Sec(f,x0,x1,epsilon,delta):
    k = 0
    iteR = 50

    if abs(f(x0)) < delta or abs(f(x1)) < delta:
        return x0 or x1

    while (k <= iteR ):

        x2 = x1 - f(x1)*((x1 - x0)/(f(x1) - f(x0)))

        print("Iteracao: %d\t x_k: %f  \tx_k+1: %f\t  x_k+2: %f\t  f(x_k+2): %f"%(k,x0,x1,x2,f(x2)))

        if (abs(x2 - x1) < epsilon or abs(f(x2)) < delta):
            return x2

        x0 = x1
        x1 = x2
        k += 1


    print("Passou do numero maximo de iteracoes")
    return x2

def f(x):
    return 0.0074*x**4 - 0.284*x**3 + 3.355*x**2 - 12.183*x + 5

def flin(x):
    return  4*0.0074*x**3 - 3*0.284*x**2 + 2*3.355*x - 12.183


raiz = Sec(f,flin,10,11,0.0001,0.0001)

print("\nRaiz = %f"%raiz)
