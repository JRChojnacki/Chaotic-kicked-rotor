 # -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:11:02 2020

@author: Janek
"""

import matplotlib.pyplot as plt
import numpy as np

def fun(p0,x0,k,n):
    x=np.zeros(n+1)
    p=np.zeros(n+1)
    x[0]=x0
    p[0]=p0
    for i in range(n):
            p[i+1]=p[i]+k*np.sin(x[i])
            x[i+1]=(x[i]+p[i+1])%(2*np.pi)
    return[x,p]
t=np.arange(51)
x1,p1=fun(1.9, 3, 1.2, 50)
x2,p2=fun(1.8999, 3, 1.2, 50)

plt.subplot(2,1,1)
plt.plot(t, x1, color='black', linestyle='-', linewidth=1)
plt.plot(t, x2, color='green', linestyle='-', linewidth=1)
plt.ylabel('X', fontsize=20)
plt.title('Położenie', fontsize=20)
plt.grid(True)
plt.legend( ('X1','X2') )

plt.subplot(2,1,2)
plt.plot(t, p1, color='black', linestyle='-', linewidth=1)
plt.plot(t, p2, color='green', linestyle='-', linewidth=1)
plt.ylabel('P', fontsize=20)
plt.title('Pęd', fontsize=20)
plt.grid(True)
plt.legend( ('P1','P2') )
#plt.savefig('trajectory.png')

