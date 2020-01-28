import matplotlib.pyplot as plt
import numpy as np
from math import pi

theta=np.loadtxt('theta.txt')
theta0=theta[1]
theta_last=theta[-1]
theta_vasat=theta[100]
theta = np.transpose(theta)
time=theta[0]
theta=theta[1:]
Nosc=np.shape(theta)[0]


plt.figure(1)
for i in range(Nosc):
    plt.plot(time,np.sin(theta[i]))



Dtheta=np.loadtxt('Dtheta.txt')
Dtheta = np.transpose(Dtheta)
Dtheta=Dtheta[1:]
plt.figure(2)
for i in range(Nosc):
    plt.plot(time,Dtheta[i])


plt.figure(3)
plt.subplot(111,polar=True)
plt.hist(theta0,np.linspace(0.,2.*pi,100),bottom=10)
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.grid(False)

plt.figure(4)
plt.subplot(111,polar=True)
plt.hist(theta_vasat,np.linspace(0.,2.*pi,100),bottom=10)
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.grid(False)


plt.figure(5)
plt.subplot(111,polar=True)
#plt.hist(theta_last,np.linspace(0.,2.*pi,100),bottom=10)
plt.hist(theta_last,bottom=10)
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.grid(False)


avr_activity=np.loadtxt('avr_activity.txt')
plt.figure(6)
plt.plot(time,avr_activity)




plt.show()
