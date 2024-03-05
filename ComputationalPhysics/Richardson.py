# Created by Yibei At 2022/11/1 Njust
from math import sin, cos ,exp
import matplotlib.pyplot as plt

def f(x):
    return sin(x)*exp(x)

def f_deriv(x):
    return cos(x)*exp(x)+sin(x)*exp(x)

# backward-difference
def f_forwd(f,x,h):
    return (f(x+h)-f(x))/h

# backward-difference
def f_backd(f,x,h):
    return (f(x)-f(x-h))/h

# backward-difference
def f_centd(f,x,h):
    return (f(x+h/2)-f(x-h/2))/h

#Richardson Extrapolation
def richar_diff(fdiff,f,x,h,p):
    richard=(2**p*fdiff(f,x,h/2)-fdiff(f,x,h))/(2**p-1)
    return richard
if __name__=="__main__":
    x=1.5
    hs = [10**(-i) for i in range(1,5)]
    d_real=f_deriv(x)
    formats = "{0:1.0e} \t{1:1.16f} \t{2:1.16f}"
    print("h   \t Forward_d error\tForward_Richardson error")
    for h in hs:
        fcentd=abs(f_forwd(f, x, h)-d_real)
        frichard=abs(richar_diff(f_forwd, f, x, h, p=1)-d_real)
        print(formats.format(h,fcentd,frichard))

    print("h   \t Center_d error \tCent_Richardson error")
    for h in hs:
        fcentd=abs(f_centd(f, x, h)-d_real)
        frichard=abs(richar_diff(f_centd, f, x, h, p=2)-d_real)
        print(formats.format(h,fcentd,frichard))