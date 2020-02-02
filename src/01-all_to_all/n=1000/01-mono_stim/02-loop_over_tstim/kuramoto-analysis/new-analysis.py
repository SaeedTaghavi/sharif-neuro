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

Dtheta=np.loadtxt('Dtheta.txt')
Dtheta = np.transpose(Dtheta)
Dtheta=Dtheta[1:]

avr_activity=np.loadtxt('avr_activity.txt')



# it_stim=200
t_stim=[]
deltaR=[]

for it_stim in range(540,640):
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

    theta_stim = np.transpose(theta_stim)
    theta_stim=theta_stim[1:]


    plt.figure(figsize=(10,10))

    gs1 = gridspec.GridSpec(21,21)
    gs1.update(left=0.1, right=0.98, wspace=0.05, hspace=0.06)
    ax1 = plt.subplot(gs1[0:6, :])
    for i in range(Nosc):
        plt.plot(time,np.sin(theta[i]))
#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin (\theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
    temp_string=r'$\sin (\theta_i)$'
    plt.ylabel(temp_string)
    plt.xticks([])

    ax2 = plt.subplot(gs1[6:12, :])
    for i in range(Nosc):
        plt.plot(time,np.sin(theta_stim[i]))

#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin( \theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
    temp_string=r'$\sin (\theta_i|_{stimulated})$'
    plt.ylabel(temp_string)
    plt.xlabel("time")


    ax3 = plt.subplot(gs1[15:21, 0:15])
    for i in range(Nosc):
        plt.plot(time,np.sin(theta_stim[i]))

#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin(\theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
    temp_string=r'$\sin (\theta_i|_{stimulated})$'
    plt.ylabel(temp_string)
    plt.xlabel("time")
    plt.xlim((it_stim-25)*dt,(it_stim+50)*dt)
    plt.annotate('stimulation', xy=((it_stim-1)*dt, 0.5), xytext=((it_stim+2)*dt, .8),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    ax4 = plt.subplot(gs1[15:21, 15:21],polar='True')
#    plt.hist(theta0, bins=np.arange(min(theta0),max(theta0),.1), bottom=10, color="black")
    n, bins, patches = plt.hist(theta_befor_stim,bins=np.arange(min(theta_after_stim),max(theta_after_stim),0.025),alpha=0.7,color="blue",bottom=10)

    plt.hist(theta_after_stim,bins=bins,alpha=0.7,color="red",bottom=10)
    plt.xticks([])
    plt.yticks([])
    filename='theta_tp={:08.4}'.format(it_stim*dt)
    extension="_.png"
    filename=filename+extension
    plt.savefig(filename,dpi=300)



#    filename='DthetaDt_tp={:08.4}'.format(it_stim*dt)
#    extension="_.txt"
#    filename=filename+extension
#    Dtheta_stim=np.loadtxt(filename)
#    Dtheta_stim = np.transpose(Dtheta_stim)
#    Dtheta_stim=Dtheta_stim[1:]
#    # plt.figure(2)
#    plt.figure()
#    plt.subplot(211)
#    for i in range(Nosc):
#        plt.plot(time,Dtheta[i])
#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\dot{\theta_i}$,  i $\in$ {1,...,'+temp_string+'}'
#    plt.ylabel(temp_string)
#
#    plt.subplot(212)
#    for i in range(Nosc):
#        plt.plot(time,Dtheta_stim[i])
#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\dot{\theta_i}$,  i $\in$ {1,...,'+temp_string+'}'
#    plt.ylabel(temp_string)
#
#    filename='DthetaDt_tp={:08.4}'.format(it_stim*dt)
#    extension="_.png"
#    filename=filename+extension
#    plt.savefig(filename)



    # plt.figure(7)
#    plt.figure()
#    plt.plot(time,order_param_r,label='not stimulated')
#    plt.plot(time,order_param_r_stim,label='stimulated')
#    plt.legend()
#    plt.ylabel(r'$r$ (order param)')

#    filename='OrderParamR_tp={:08.4}'.format(it_stim*dt)
#    extension="_.png"
#    filename=filename+extension
#    plt.savefig(filename)
    
    
#    filename='AvrActivity_tp={:08.4}'.format(it_stim*dt)
#    extension="_.txt"
#    filename=filename+extension
#    avr_activity_stim=np.loadtxt(filename)
#    plt.figure()    
#    #plt.figure(6)
#    plt.plot(time,avr_activity_stim,label='stimulated')
#    plt.plot(time,avr_activity,label='not stimulated')
#    plt.ylabel(r'$f$ (average activity)')

#    filename='AvrActivity_tp={:08.4}'.format(it_stim*dt)
#    extension="_.png"
#    filename=filename+extension
#    plt.savefig(filename)
    
#    # plt.show()
    print (it_stim, "  done!")
    plt.close('all')

#plt.figure()
#plt.plot(t_stim,deltaR)
#plt.ylabel(r'$ \Delta r = (r-r_{stim})\|_{t_{stim}} $')
#plt.savefig('deltaR.png')

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
