import numpy as np
from math import pi


def derives(Nosc,K,theta,omega0):
    for i in range(Nosc):
        sigma = 0.0
        for j in range(Nosc):
            sigma = sigma + np.sin(theta[j]-theta[i])
        sigma = sigma *K/Nosc
        sigma = sigma + omega0[i]
        DthetaDt[i]=sigma
    return DthetaDt

def integrate_one_step(X,DxDt,dt):
    X=X+(dt*DxDt)
    return X

def func_average_activity(Nosc,theta):
    f = 0.0
    for i in range(Nosc):
        f = f + np.cos(theta[i])
    f = f / Nosc
    return f

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


np.random.seed(3) 
  
K=.70
Nosc=60
dt = .1

theta0 = np.random.uniform(0.0,2.0*pi,Nosc)
omega0 = np.random.uniform(.5,1.0,Nosc)
#omega0 = np.append(np.random.uniform(0.,1.0,Nosc/2),omega0)


tp=250
theta=theta0
DthetaDt=np.zeros(Nosc)
thetas=[]
Dthetas=[]
average_activity=[]
r_prev,psi_prev=calc_order_param(Nosc,theta0)
for t in range(1500):
    DthetaDt = derives(Nosc,K,theta,omega0)
    r,psi=calc_order_param(Nosc,theta)
#    if (t==tp):# or t==250 or t == 360 or t==410 or t==450 or t== 520):
#        DthetaDt = DthetaDt - 5.*np.sin(theta)
#    if (abs( np.cos(psi)+ 0.7 )<0.01):
#        if (np.cos(psi)<np.cos(psi_prev)):
#            DthetaDt = DthetaDt - 5.*np.sin(theta)
#    if ( np.cos(psi)<- 0.8):
#        if (np.cos(psi_prev)>-0.8):
#            DthetaDt = DthetaDt - 5.*np.sin(theta)

    psi_prev=psi; r_prev=r
    theta=integrate_one_step(theta,DthetaDt,dt)
    # np.savetxt(file_theta,(theta[0],theta[1],theta[2]),fmt='%1.4e')
    time_theta=np.insert(theta,0,t*dt)
    time_Dtheta=np.insert(DthetaDt,0,t*dt)
    time_avr_activity = func_average_activity(Nosc,theta)
    average_activity.append(time_avr_activity)
    thetas.append(time_theta)
    Dthetas.append(time_Dtheta)

filename='theta_tp={:08.4}'.format(tp*dt)
extension="_.txt"
filename=filename+extension
file_theta=open(filename,"w+")
np.savetxt(file_theta,thetas)
file_theta.close()

file_Dtheta=open("Dtheta.txt","w+")
np.savetxt(file_Dtheta,Dthetas)
file_Dtheta.close()

file_avr_activity=open("avr_activity.txt","w+")
np.savetxt(file_avr_activity,average_activity)
file_avr_activity.close()
