from math import sin, cos ,exp
import matplotlib.pyplot as plt

def f(x):
    return sin(x)*exp(x)

def f_deriv(x):
    return cos(x)*exp(x)+sin(x)*exp(x)

# backward-difference
def f_forw(f,x,h):
    return (f(x+h)-f(x))/h

# backward-difference
def f_back(f,x,h):
    return (f(x)-f(x-h))/h

# backward-difference
def f_cent(f,x,h):
    return (f(x+h/2)-f(x-h/2))/h

if __name__=="__main__":
    x=0.5
    hs = [10**(-i) for i in range(1, 11)]
    fd=f_deriv(x)
    fford=[abs(f_forw(f,x,h)-fd) for h in hs]
    fback = [abs(f_back(f, x, h) - fd) for h in hs]
    fcent = [abs(f_cent(f, x, h) - fd) for h in hs]
    print(hs,fford,fback,fcent)
    plt.plot(hs,fford,label="Forward")
    plt.plot(hs, fback, label="Backward")
    plt.plot(hs, fcent, label="Center")
    plt.yscale('log')
    plt.xscale('log')
    plt.legend()
    plt.show()
