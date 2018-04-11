import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

ki, n, k1, k2, k3, k4, k5 = 1, 5, 5, 20, 5, 5, 2
func = lambda x: k2/(1+(x/ki)**n)

def dsdt(S,t,f=func):
    return [k1+k5*S[1]-k3*S[0],f(S[0])-k5*S[1]-k4*S[1]]
t = np.linspace(0,1.5,200)

for x in [(0,0),(0.25,2),(2,2),(2,0.25)]:
    S0 = [x[0],x[1]]
    y = odeint(dsdt, S0, t)
    plt.plot(y[:, 0], y[:, 1])

x1, y1 = np.meshgrid(np.linspace(0,3,15),np.linspace(0,3,15))
dx1,dy1 = dsdt([x1,y1],t)
M = np.hypot(dx1,dy1) # equals to (dx1**2+dy1**2)**0.5
M = (dx1**2+dy1**2)**0.5
M[M==0] = 1
dx1 /= M
dy1 /= M

plt.quiver(x1,y1,dx1,dy1,width=0.0025)

nu1 = np.linspace(0,3)
plt.plot(nu1,(-k1+k3*nu1)/k5,"k:")
plt.plot(nu1,func(nu1)/(k4+k5),"k:")
plt.axis([0,3,0,3])
plt.xlabel(r"$S_1$")
plt.ylabel(r"$S_2$")
plt.show()