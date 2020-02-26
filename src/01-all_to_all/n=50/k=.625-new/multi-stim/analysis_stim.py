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
theta_stim=np.loadtxt('theta_stim.txt')
Nosc=np.shape(np.transpose(theta))[0]-1
Ntime=np.shape(np.transpose(theta))[1]

theta0=theta[1]
theta_last=theta[-1]
theta_vasat=theta[100]
order_param_r=np.zeros(Ntime)
order_param_psi=np.zeros(Ntime)
order_param_r_stim=np.zeros(Ntime)
order_param_psi_stim=np.zeros(Ntime)
for t in range(Ntime):
    order_param_r[t],order_param_psi[t]=calc_order_param(Nosc,theta[t])
    order_param_r_stim[t],order_param_psi_stim[t]=calc_order_param(Nosc,theta_stim[t])


theta = np.transpose(theta)
theta_stim = np.transpose(theta_stim)
time=theta[0]
theta=theta[1:]


plt.figure(1)
for i in range(Nosc):
    plt.plot(time,np.sin(theta_stim[i]))

plt.figure(7)
plt.plot(time,order_param_r)
plt.plot(time,order_param_r_stim)
plt.ylabel('order param r')

plt.show()

