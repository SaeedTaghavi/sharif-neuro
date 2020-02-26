import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.rcParams.update({'font.size': 18})
import numpy as np
import matplotlib.mlab as mlab
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
#theta_vasat=theta[100]
order_param_r=np.zeros(Ntime)
order_param_psi=np.zeros(Ntime)
mean_theta=np.zeros(Ntime)
for t in range(Ntime):
    order_param_r[t],order_param_psi[t]=calc_order_param(Nosc,theta[t])
    mean_theta[t]=np.mean(theta[t])

theta = np.transpose(theta)
time=theta[0]
theta=theta[1:]

dt=time[1]-time[0]
np.savetxt("times.txt",time[540:640])
np.savetxt("mean_thetas.txt",mean_theta[540:640])
np.savetxt("order_param_psi.txt",order_param_psi[540:640])
exit()
