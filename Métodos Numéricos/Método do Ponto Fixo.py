import numpy as np

def PF(x0,epsilon,delta,phi,f):
    iterM = 200

    for k in range(0,iterM):

        x1 = phi(x0)

        print("Iteracao: %d\t x_k: %f \tx_k+1: %f\t f(x_k+1): %f"%(k,x0,x1,f(x1)))

        if abs(x1-x0) < epsilon or abs(f(x1)) < delta:
            return x1

        x0 = x1

def phi(x):
    return np.exp(-1*0.5 * x) * (4 - x) - 2 + x
    
def f(x):
    return np.exp(-1*0.5 * x) * (4 - x) - 2

raiz = PF(100,0.0001,0.0001,phi,f)
print("Raiz = {}".format(raiz))
