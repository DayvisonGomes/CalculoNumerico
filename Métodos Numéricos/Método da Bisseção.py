Import numpy as np


def Bissec(a0,b0,epsilon,f):
    iterM = 20
    a = []
    b = []
    x = []
    a.append(a0)
    b.append(b0)

    for k in range(0,iterM):

        imgA = f(a[k])
        imgB = f(b[k])

        x.append((b[k] + a[k])/2)
        imgX = f(x[k])

        print("f(a[%d]) = %f \t f(b[%d]) = %f \t  f(x[%d]) = %f \t x[%d] = %f \t a[%d] = %f \t b[%d] = %f"%(k,imgA,k,imgB,k,imgX,k,x[k],k,a[k],k,b[k]))

        if abs(f(x[k]))  == 0:
            return x[k]

        if abs(f(x[k])) < epsilon:
            return x[k]

        if abs(b[k] - a[k]) < epsilon:
            return x[k]

        if imgX*imgA < 0:
            a.append(a[k])
            b.append(x[k])

        else:
            a.append(x[k])
            b.append(b[k])

def f(x):
    return 1-((400*(3+x))/(9.81*(3*x + x**2/2)**3))

raiz = Bissec(0.4,2.4,0.001,f)

print("\nRaiz = {}".format(raiz))

