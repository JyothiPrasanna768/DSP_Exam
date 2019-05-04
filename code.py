import random as rand
import subprocess
import numpy as np
import matplotlib.pyplot as plt
with open('/home/rgukt/Desktop/DSP_lab_end_sem/radar.txt','r') as f:
     data=f.read()

from StringIO import StringIO
in_data	=StringIO(data)

data=np.genfromtxt(in_data,dtype=int,delimiter=",")

def add(a,b):
    c=a+b
    return c

n=len(data)
print('length of data:',n)
w_n=np.random.rand(n)
#print(w_n)
x=[]
n0=100
for i in range(0,n+n0,1):
    if (i-n0)<=0:
       a=0
       x.append(a)
    else:
       a=data[i-n0]
       x.append(a)
#x_n_n0=np.array(x)
print('length of x[n-n0]',len(x))

###############
w_z=[]
n0=100
for i in range(0,n+n0,1):
    if (i-n0)<=0:
       a=0
       w_z.append(a)
    else:
       a=w_n[i-n0]
       w_z.append(a)
#w_n_n0=np.array(w_z)

print('length of noise w[n-n0]',len(w_z))
###############
y_n=[]

for i in range(0,n+n0,1):
    b=add((x[i]),(w_z[i]))
    y_n.append(b)
    i=i+1
y_n_n0=np.array(y_n)
#print(y_n_n0)
#print('length of y[n-n0]',len(y_n_n0))

h=[]
for i in range(0,n+n0,1):
	a=y_n[n-i-1]
	h.append(a)
print(h)	

def convolute(x,h):
    n1=len(x)
    n2=len(h)
    print(n1,n2)
    y=[]
    for n in range(n1+n2-1):
          sum=0
          for k in range(n1):
             if n-k>=0 and n-k<=n2-1:
                   sum=sum+x[k]*h[n-k]
          y=np.append(y,sum)
    plt.stem(y)
    plt.show()
    return y

print('convolute',convolute(x,h))
