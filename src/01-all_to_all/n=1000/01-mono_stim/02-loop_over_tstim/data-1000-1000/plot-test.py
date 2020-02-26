import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.rcParams.update({'font.size': 18})
import numpy as np
import matplotlib.mlab as mlab
from math import pi

deltaR=np.loadtxt('deltaR.txt')
mean_theta=np.loadtxt("mean_thetas.txt")
t_stim=np.loadtxt('t_stim.txt')
time=np.loadtxt("times.txt")

plt.figure(figsize=(10,10))
plt.plot(t_stim,-10*deltaR,label=r"$\Delta r$")
plt.plot(time, -np.sin(mean_theta),label=r"$\Sigma \theta / N$")

plt.xlabel('time')
plt.ylabel(r'$ \Delta r = (r_{stim}-r)\|_{t_{stim}} $')
plt.legend()
plt.savefig('deltaR.png')






# Create some mock data

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time')
ax1.set_ylabel(r'$\Delta r = r_{stim} - r$', color=color)
ax1.plot(t_stim, -deltaR, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel(r'$Z (\theta_{mean})=-\sin (\theta_{mean})$', color=color)  # we already handled the x-label with ax1
#ax2.plot(time+0.8, -np.sin(mean_theta), color=color)
#ax2.plot(time, -np.sin(mean_theta), color=color)
ax2.plot(time, -np.cos(mean_theta), color='black')
ax2.tick_params(axis='y', labelcolor='black')
#ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('deltaR-Z.png')
#plt.show()



fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time')
ax1.set_ylabel(r'$ 40 \times\Delta r $', color=color)
ax1.plot(t_stim, -37*deltaR, color=color)
ax1.plot(t_stim, -deltaR, '-.', color=color)
#ax1.tick_params(axis='y', labelcolor=color)

color = 'tab:blue'
#ax2.plot(time+0.8, -np.sin(mean_theta), color=color)
#ax2.plot(time, -np.sin(mean_theta), color=color)
dt=time[2]-time[1]
moshtagh=np.zeros(np.size(time)-1)
for i in range(np.size(time)-1):
    moshtagh[i]=(-np.sin(mean_theta[i+1])+np.sin(mean_theta[i]))/(dt)

#ax1.plot(time[0:99], moshtagh)
ax1.plot(time, -np.sin(mean_theta) , color=color)
ax1.tick_params(axis='y', labelcolor='black')
#ax2.tick_params(axis='y', labelcolor=color)

ax1.plot(time,np.zeros_like(time),color='black')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('deltaR+Z.png')


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
