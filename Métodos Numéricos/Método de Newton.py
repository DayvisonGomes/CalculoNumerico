import math
import numpy as np
from numpy import *
from sympy import *

def Newton(f,flin,x0,epsilon,delta):
    k = 0
    iteR = 200

    if abs(f(x0)) < delta:
        return x0

    while (k <= iteR ):

        x1 = x0 - (f(x0)/flin(x0))

        print("Iteracao: %d\t x_k: %f \tx_k+1: %f\t f(x_k+1): %f"%(k,x0,x1,f(x1)))

        if (abs(x1 - x0) < epsilon or abs(f(x1)) < delta):
            return x1

        x0 = x1
        k += 1


    print("Passou do numero maximo de iteracoes")
    return x1

def f(x):
    return 320000/(1+31*np.exp(-0.09*x)) - 1.6*(80000*np.exp(-0.05*x)+110000)

def flin(x):
    return  (320000*31*0.09*np.exp(-0.09*x))/(1+31*np.exp(-0.09*x))**2 + 1.6*80000*0.05*np.exp(-0.05*x)

def gsub(x):
    return 320000/(1+31*np.exp(-0.09*x))

def zurb(x):
    return (80000*np.exp(-0.05*x)+110000)

raiz = Newton(f,flin,40,0.001,0.001)

print("\nRaiz = %f"%raiz)

print("\nSubUrbano = %f \nUrbano = %f"%(gsub(raiz),zurb(raiz)))
