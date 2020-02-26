import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.rcParams.update({'font.size': 16})
import numpy as np
import matplotlib.mlab as mlab
from math import pi


label_fsize=18
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

#Dtheta=np.loadtxt('Dtheta.txt')
#Dtheta = np.transpose(Dtheta)
#Dtheta=Dtheta[1:]

#avr_activity=np.loadtxt('avr_activity.txt')



# it_stim=200


#for it_stim in range(540,640):
#for it_stim in range(540,541):
it_stim=557
filename='theta_tp={:08.4}'.format(it_stim*dt)
extension="_.txt"
filename=filename+extension
theta_stim_557=np.loadtxt(filename)

order_param_r_stim_557=np.zeros(Ntime)
order_param_psi_stim_557=np.zeros(Ntime)
theta_befor_stim_557 = theta_stim_557[it_stim-1]
theta_befor_stim_557 = theta_befor_stim_557[1:]
theta_after_stim_557 = theta_stim_557[it_stim]
theta_after_stim_557 = theta_after_stim_557[1:]
for t in range(Ntime):
    order_param_r_stim_557[t],order_param_psi_stim_557[t]=calc_order_param(Nosc,theta_stim_557[t])

theta_stim_557 = np.transpose(theta_stim_557)
theta_stim_557=theta_stim_557[1:]


it_stim=593
filename='theta_tp={:08.4}'.format(it_stim*dt)
extension="_.txt"
filename=filename+extension
theta_stim_593=np.loadtxt(filename)

order_param_r_stim_593=np.zeros(Ntime)
order_param_psi_stim_593=np.zeros(Ntime)
theta_befor_stim_593 = theta_stim_593[it_stim-1]
theta_befor_stim_593 = theta_befor_stim_593[1:]
theta_after_stim_593 = theta_stim_593[it_stim]
theta_after_stim_593 = theta_after_stim_593[1:]
for t in range(Ntime):
    order_param_r_stim_593[t],order_param_psi_stim_593[t]=calc_order_param(Nosc,theta_stim_593[t])

theta_stim_593 = np.transpose(theta_stim_593)
theta_stim_593=theta_stim_593[1:]



plt.figure(figsize=(8,11.5))
gs1 = gridspec.GridSpec(42,21)
gs1.update(left=0.12, right=0.98, wspace=0.05, hspace=0.25)



ax1 = plt.subplot(gs1[0:7, :])
for i in range(Nosc):
    plt.plot(time,np.sin(theta[i]))
#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin (\theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
temp_string=r'$\sin (\theta_i)$'
plt.ylabel(temp_string,fontsize=label_fsize)
plt.xlim(0,70)
plt.xticks([])
plt.yticks([-.90,0.0,.90])
plt.ylim(-1.1,1.1)
plt.title('(a)', loc='left')



ax2 = plt.subplot(gs1[7:14, :])
for i in range(Nosc):
    plt.plot(time,np.sin(theta_stim_557[i]))

#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin( \theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
temp_string=r'$\sin (\theta_i|_{stim})$'
plt.ylabel(temp_string,fontsize=label_fsize)
plt.xlim(0,70)
plt.xticks([])
plt.yticks([-.90,0.0,.90])
plt.ylim(-1.1,1.1)


ax3 = plt.subplot(gs1[14:21, :])
for i in range(Nosc):
    plt.plot(time,np.sin(theta_stim_593[i]))

#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin( \theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
temp_string=r'$\sin (\theta_i|_{stim})$'
plt.ylabel(temp_string,fontsize=label_fsize)
plt.xlabel("time",fontsize=label_fsize)
plt.xlim(0,70)
plt.yticks([-.90,0.0,.90])
plt.ylim(-1.1,1.1)	

#[21:24]empty

ax4 = plt.subplot(gs1[25:32, 0:12])
for i in range(Nosc):
    plt.plot(time,np.sin(theta_stim_557[i]))

#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin(\theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
temp_string=r'$\sin (\theta_i|_{stim})$'
plt.ylabel(temp_string,fontsize=label_fsize)
#plt.xlabel("time",fontsize=label_fsize)
it_stim=557
plt.xlim((it_stim-25)*dt,(it_stim+50)*dt)
plt.xticks([55,56,58,60])
plt.annotate('stimulation', xy=((it_stim-1)*dt, 0.5), xytext=((it_stim+8)*dt, .8), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.title('(b)', loc='left')



ax5 = plt.subplot(gs1[24:33, 12:21],polar='True')
theta_befor_stim_557 = theta_befor_stim_557 % (2*pi)
#    plt.hist(theta0, bins=np.arange(min(theta0),max(theta0),.1), bottom=10, color="black")
plt.hist(theta_befor_stim_557, bins=np.arange(min(theta_befor_stim_557),max(theta_befor_stim_557),.05), bottom=200, color="blue",alpha=.5)
#    n, bins, patches = plt.hist(theta_befor_stim,bins=np.arange(min(theta_after_stim),max(theta_after_stim),0.025),alpha=0.7,color="blue")
theta_after_stim_557 = theta_after_stim_557 % (2*pi)
#    plt.hist(theta_after_stim,bins=bins,alpha=0.7,color="red",bottom=10)
plt.hist(theta_after_stim_557, bins=np.arange(min(theta_after_stim_557),max(theta_after_stim_557),.05), bottom=200, color="red",alpha=.5)
ax5.axis('off')
plt.xticks([])
plt.grid(True)
ax5.set_yticklabels([])
plt.plot(np.linspace(0,2*pi,1000),200*np.ones(1000),'black',lw=.6)
plt.ylim(0, 365)
plt.title('(c)', loc='left')





ax6 = plt.subplot(gs1[34:41, 0:12])
for i in range(Nosc):
    plt.plot(time,np.sin(theta_stim_593[i]))

#    temp_string="{:2}".format(Nosc)
#    temp_string=r'$\sin(\theta_i)$,  i $\in$ {1,...,'+temp_string+'}'
temp_string=r'$\sin (\theta_i|_{stim})$'
plt.ylabel(temp_string,fontsize=label_fsize)
plt.xlabel("time",fontsize=label_fsize)
it_stim=593
plt.xlim((it_stim-25)*dt,(it_stim+50)*dt)
plt.annotate('stimulation', xy=((it_stim-1)*dt, -0.5), xytext=((it_stim+2)*dt, -.8), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.title('(d)', loc='left')


ax7 = plt.subplot(gs1[33:42, 12:21],polar='True')
theta_befor_stim_593 = theta_befor_stim_593 % (2*pi)
#    plt.hist(theta0, bins=np.arange(min(theta0),max(theta0),.1), bottom=10, color="black")
plt.hist(theta_befor_stim_593, bins=np.arange(min(theta_befor_stim_593),max(theta_befor_stim_593),.05), bottom=200, color="blue",alpha=.5)
#    n, bins, patches = plt.hist(theta_befor_stim,bins=np.arange(min(theta_after_stim),max(theta_after_stim),0.025),alpha=0.7,color="blue")
theta_after_stim_593 = theta_after_stim_593 % (2*pi)
#    plt.hist(theta_after_stim,bins=bins,alpha=0.7,color="red",bottom=10)
plt.hist(theta_after_stim_593, bins=np.arange(min(theta_after_stim_593),max(theta_after_stim_593),.05), bottom=200, color="red",alpha=.5)
ax7.set_yticklabels([])
ax7.axis('off')
plt.xticks([])
ax7.set_yticklabels([])
plt.plot(np.linspace(0,2*pi,1000),200*np.ones(1000),'black',lw=.6)
plt.plot([0,0],[200,200],'b-')
#plt.plot(np.linspace(0,2*pi,1000),365*np.ones(1000),'black',lw=.6)
plt.ylim(0, 365)
#plt.yticks([])
plt.title('(e)', loc='left')

filename='theta_tp={:08.4}'.format(it_stim*dt)
extension="_last.png"
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



#plt.figure(7)
deltaR=np.loadtxt('deltaR.txt')
t_stim=np.loadtxt('t_stim.txt')
plt.figure(figsize=(10,8))
plt.plot(time,order_param_r_stim_557,label=r'$t_{stim}$=55.7')
plt.plot(time,order_param_r_stim_593,label=r'$t_{stim}$=59.3')
plt.plot(time,order_param_r,label='not stimulated')
plt.plot(t_stim,-deltaR+order_param_r[540:640],label=r'$\Delta r$')
#plt.annotate(r'$\Delta r$', xy=((557-1)*dt, order_param_r_stim_557[557]+0.01), xytext=((350)*dt, .8), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#plt.annotate('', xy=((593-1)*dt, order_param_r_stim_593[593]-0.01), xytext=((400)*dt, .82), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-.2"))
plt.legend()
plt.ylabel(r'$r$ (order param)')
plt.xlabel('time')

 # location for the zoomed portion 
sub_axes = plt.axes([.25, .35, .4, .4]) 

# plot the zoomed portion

order_param_r_stim_557_det=order_param_r_stim_557[540:640]
order_param_r_stim_593_det=order_param_r_stim_593[540:640]
order_param_r_det=order_param_r[540:640]
time_det=time[540:640]
sub_axes.plot(time_det,order_param_r_stim_557_det,label=r'$t_{stim}$=55.7')
sub_axes.plot(time_det,order_param_r_stim_593_det,label=r'$t_{stim}$=59.3')
sub_axes.plot(time_det,order_param_r_det,label='not stimulated')
sub_axes.plot(t_stim,-deltaR+order_param_r[540:640],label=r'$\Delta r$')



filename='OrderParamR_tp={:08.4}'.format(it_stim*dt)
extension="_last.png"
filename=filename+extension
plt.savefig(filename)



plt.figure(figsize=(10,8))
plt.plot(time,order_param_r_stim_557,label=r'$t_{stim}$=55.7',color='#1f77b4')
plt.plot(time,order_param_r,label='not stimulated',color='green')
plt.legend()
plt.ylabel(r'$r$ (order param)')
plt.xlabel('time')
# location for the zoomed portion 
sub_axes = plt.axes([.25, .35, .4, .4]) 
# plot the zoomed portion
order_param_r_stim_557_det=order_param_r_stim_557[540:640]
order_param_r_det=order_param_r[540:640]
time_det=time[540:640]
sub_axes.plot(time_det,order_param_r_stim_557_det,label=r'$t_{stim}$=55.7',color='#1f77b4')
sub_axes.plot(time_det,order_param_r_det,label='not stimulated',color='green')
plt.ylim(0.91,0.99)
plt.xlim(54,64)
filename='OrderParamR_only_tp={:08.4}'.format(557*dt)
extension="_last.png"
filename=filename+extension
plt.savefig(filename)




plt.figure(figsize=(10,8))
plt.plot(time,order_param_r_stim_593,label=r'$t_{stim}$=59.3',color='orange')
plt.plot(time,order_param_r,label='not stimulated',color='green')
plt.legend()
plt.ylabel(r'$r$ (order param)')
plt.xlabel('time')
# location for the zoomed portion 
sub_axes = plt.axes([.25, .35, .4, .4]) 
# plot the zoomed portion
order_param_r_stim_593_det=order_param_r_stim_593[540:640]
order_param_r_det=order_param_r[540:640]
time_det=time[540:640]
sub_axes.plot(time_det,order_param_r_stim_593_det,label=r'$t_{stim}$=59.3',color='orange')
sub_axes.plot(time_det,order_param_r_det,label='not stimulated',color='green')
plt.ylim(0.91,0.99)
plt.xlim(54,64)
#inja
filename='OrderParamR_only_tp={:08.4}'.format(593*dt)
extension="_last.png"
filename=filename+extension
plt.savefig(filename)


    
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


