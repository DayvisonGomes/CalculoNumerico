import numpy as np

def FP(a0,b0,epsilon,f):
    iterM = 100
    a = []
    b = []
    x = []
    a.append(a0)
    b.append(b0)

    for k in range(0,iterM):

        imgA = f(a[k])
        imgB = f(b[k])

        x.append(a[k] - ((b[k] - a[k])/(f(b[k]) - f(a[k])))*f(a[k]))
        imgX = f(x[k])

        print("f(a[%d]) = %f \t f(b[%d]) = %f \t  f(x[%d]) = %f \t x[%d] = %f \t a[%d] = %f \t b[%d] = %f"%(k,imgA,k,imgB,k,imgX,k,x[k],k,a[k],k,b[k]))

        if abs(b[k] - a[k]) < epsilon:
            return x[k]

        if abs(f(x[k])) < epsilon:
            return x[k]

        elif imgX*imgA < 0:
            a.append(a[k])
            b.append(x[k])

        else:
            a.append(x[k])
            b.append(b[k])


def f(x):
    return 320000/(1+31*np.exp(-0.09*x)) - 1.6*(80000*np.exp(-0.05*x)+110000)

def gsub(x):
    return 320000/(1+31*np.exp(-0.09*x))

def zurb(x):
    return (80000*np.exp(-0.05*x)+110000)

raiz = FP(40,45,0.001,f)

print("\nRaiz = %f"%(raiz))

print("\nSubUrbano = %f \nUrbano = %f"%(gsub(raiz),zurb(raiz)))


