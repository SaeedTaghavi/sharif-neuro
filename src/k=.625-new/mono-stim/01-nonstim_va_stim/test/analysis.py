import matplotlib.pyplot as plt
import numpy as np
from math import pi

def calc_order_param(Nos,theta):
    real_sum=0.0
    img_sum=0.0
    r=0.0
    psi=0.0
    for i in range(Nosc):
        real_sum = real_sum+np.cos(theta[i])
        img_sum = img_sum+np.sin(theta[i])
    real_sum=real_sum/Nosc
    img_sum=img_sum/Nosc
    r=np.sqrt(real_sum*real_sum+img_sum*img_sum)
    psi = np.arccos(real_sum/r)
    return r,psi


theta=np.loadtxt('theta.txt')
Nosc=np.shape(np.transpose(theta))[0]-1
Ntime=np.shape(np.transpose(theta))[1]

theta0=theta[1]
theta_last=theta[-1]
theta_vasat=theta[100]
order_param_r=np.zeros(Ntime)
order_param_psi=np.zeros(Ntime)
for t in range(Ntime):
    order_param_r[t],order_param_psi[t]=calc_order_param(Nosc,theta[t])


theta = np.transpose(theta)
time=theta[0]
theta=theta[1:]


plt.figure(1)
for i in range(Nosc):
    plt.plot(time,np.sin(theta[i]))
temp_string="{:2}".format(Nosc)
temp_string=r'$\theta_i$,  i $\in$ {1,...,'+temp_string+'}'
plt.ylabel(temp_string)


plt.figure(7)
plt.plot(time,order_param_r)
plt.ylabel(r'$r$ (order param)')

#plt.show();exit()

Dtheta=np.loadtxt('Dtheta.txt')
Dtheta = np.transpose(Dtheta)
Dtheta=Dtheta[1:]

plt.figure(2)
for i in range(Nosc):
    plt.plot(time,Dtheta[i])
temp_string="{:2}".format(Nosc)
temp_string=r'$\dot{\theta_i}$,  i $\in$ {1,...,'+temp_string+'}'
plt.ylabel(temp_string)

plt.show();exit()



#plt.figure(3)
#plt.subplot(111,polar=True)
#plt.hist(theta0,np.linspace(0.,2.*pi,100),bottom=10)
#plt.xticks([])
#plt.yticks([])
#plt.axis('off')
#plt.grid(False)

#plt.figure(4)
#plt.subplot(111,polar=True)
#plt.hist(theta_vasat,np.linspace(0.,2.*pi,100),bottom=10)
#plt.xticks([])
#plt.yticks([])
#plt.axis('off')
#plt.grid(False)


#plt.figure(5)
#plt.subplot(111,polar=True)
##plt.hist(theta_last,np.linspace(0.,2.*pi,100),bottom=10)
#plt.hist(theta_last,bottom=10)
#plt.xticks([])
#plt.yticks([])
#plt.axis('off')
#plt.grid(False)


avr_activity=np.loadtxt('avr_activity.txt')
plt.figure(6)
plt.plot(time,avr_activity)
plt.ylabel(r'$f$ (average activity)')


plt.figure(8)
plt.subplot(211)
plt.plot(time,np.sin(order_param_psi))
plt.subplot(212)
plt.plot(time,np.cos(order_param_psi))
plt.show()
