# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:23:59 2020

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
            p[i+1]=(p[i]+k*np.sin(x[i]))%(2*np.pi)
            x[i+1]=(x[i]+p[i+1])%(2*np.pi)
    return[x,p]
X=[]
P=[]
for i in range(1000):
   x0, p0 = np.random.ranf(2)*2*np.pi
   X[i],P[i]=fun(p0,x0,1.1,1000)
   r, g, b = np.random.ranf(3)
plt.plot(X, P, ',', color=(r,g,b) ) 
plt.xlim(0,6) 
#plt.ylim(0,6)
plt.xlabel('X', fontsize=20)
plt.ylabel('P', fontsize=20)
plt.title('Phase space portrait for K=0', fontsize=20)
#plt.savefig('PhasePortrait0.png')
    
