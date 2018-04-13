import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

a,b,c,d = 1, 1, 1, 1

def dSdt(S,t,a=a,b=b,c=c,d=d):
    """
        differentiation of x and y
        :return: dxdt, dydt
        """
    return [a*S[0]-b*S[0]*S[1],-c*S[1]+d*S[0]*S[1]]

def setup_plot(num,lis):
    """
        :param num: number of subplots
        :param lis: [xlabel, ylabel]
        :return: subplots(objects)
        """
    plt.figure(1,figsize=(8,6*num))
    sub = []
    for i in range(num):
        locals()["a%s" % (i + 1)] = plt.subplot("%d1%d" % (num, i))
        locals()["a%s" % (i + 1)].set_xlabel(lis[i][0])
        locals()["a%s" % (i + 1)].set_ylabel(lis[i][1])
        sub.append(locals()["a%s" % (i + 1)])
    return sub


t = np.linspace(0,10,1000)
S0 = [2,1]
y = odeint(dSdt,S0,t)

xylabel = [["population of preys","population of predators"],["Time","population"]]
a2, a1 = setup_plot(2,xylabel)

a1.plot(y[:,0],y[:,1],label="relation")
a2.plot(t,y[:,0],"k--",label="preys")
a2.plot(t,y[:,1],"k-",label="predators")

a1.legend()
a2.legend()
plt.show()
