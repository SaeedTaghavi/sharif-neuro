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
for t in range(Ntime):
    order_param_r[t],order_param_psi[t]=calc_order_param(Nosc,theta[t])

theta = np.transpose(theta)
time=theta[0]
theta=theta[1:]

dt=time[1]-time[0]

t_stim=[]
deltaR=[]

for it_stim in range(540,640):
#for it_stim in range(540,541):
    filename='theta_tp={:08.4}'.format(it_stim*dt)
    extension="_.txt"
    filename=filename+extension
    theta_stim=np.loadtxt(filename)

    order_param_r_stim=np.zeros(Ntime)
    order_param_psi_stim=np.zeros(Ntime)
    theta_befor_stim = theta_stim[it_stim-1]
    theta_befor_stim = theta_befor_stim[1:]
    theta_after_stim = theta_stim[it_stim]
    theta_after_stim = theta_after_stim [1:]
    for t in range(Ntime):
        order_param_r_stim[t],order_param_psi_stim[t]=calc_order_param(Nosc,theta_stim[t])
    deltaR.append(order_param_r[it_stim]-order_param_r_stim[it_stim])
    t_stim.append(it_stim*dt)
    print(it_stim,"done!")

np.savetxt('deltaR.txt',deltaR)
np.savetxt('t_stim.txt',t_stim)
plt.figure()
plt.plot(t_stim,deltaR)
plt.ylabel(r'$ \Delta r = (r-r_{stim})\|_{t_{stim}} $')
plt.savefig('deltaR.png')

exit()



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



plt.figure(8)
plt.subplot(211)
plt.plot(time,np.sin(order_param_psi))
plt.subplot(212)
plt.plot(time,np.cos(order_param_psi))
plt.show()
