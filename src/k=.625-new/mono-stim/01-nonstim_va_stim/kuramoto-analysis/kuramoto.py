import numpy as np
from math import pi

def derives(Nosc,K,theta,omega0):
    DthetaDt=np.zeros(Nosc)
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
  
K=.45
Nosc=50
dt = 0.1

theta0 = np.random.uniform(0.0,2.0*pi,Nosc)
#omega0 = np.random.uniform(0.9,1.0,Nosc)
omega0 = np.random.normal(1.0, 0.1, Nosc)
theta=theta0
DthetaDt=np.zeros(Nosc)
thetas=[]
Dthetas=[]
average_activity=[]
r_prev,psi_prev=calc_order_param(Nosc,theta0)

theta_stim=theta0
DthetaDt_stim=np.zeros(Nosc)
thetas_stim=[]
Dthetas_stim=[]
average_activity_stim=[]
r_prev_stim,psi_prev_stim=calc_order_param(Nosc,theta0)

for t in range(1000):
    DthetaDt = derives(Nosc,K,theta,omega0)
    r, psi = calc_order_param(Nosc,theta)

    DthetaDt_stim = derives(Nosc,K,theta_stim,omega0)
    r_stim, psi_stim = calc_order_param(Nosc,theta_stim)
    if (t==260 or t==325 or t==386 or t == 447 or t == 508 or t==572 or t==635):
        DthetaDt_stim = DthetaDt_stim - 5.*np.sin(theta_stim)
#    if (abs( np.cos(psi)+ 0.7 )<0.01):
#        if (np.cos(psi)<np.cos(psi_prev)):
#            DthetaDt = DthetaDt - 5.*np.sin(theta)
#    if ( np.cos(psi)<- 0.8):
#        if (np.cos(psi_prev)>-0.8):
#            DthetaDt = DthetaDt - 5.*np.sin(theta)

#    psi_prev=psi; r_prev=r
    theta=integrate_one_step(theta,DthetaDt,dt)
    time_theta=np.insert(theta,0,t*dt)
    time_Dtheta=np.insert(DthetaDt,0,t*dt)
    time_avr_activity = func_average_activity(Nosc,theta)
    average_activity.append(time_avr_activity)
    thetas.append(time_theta)
    Dthetas.append(time_Dtheta)
    
    theta_stim=integrate_one_step(theta_stim,DthetaDt_stim,dt)
    time_theta_stim=np.insert(theta_stim,0,t*dt)
    time_Dtheta_stim=np.insert(DthetaDt_stim,0,t*dt)
    time_avr_activity_stim = func_average_activity(Nosc,theta_stim)
    average_activity_stim.append(time_avr_activity_stim)
    thetas_stim.append(time_theta_stim)
    Dthetas_stim.append(time_Dtheta_stim)

file_theta=open("theta.txt","w+")
np.savetxt(file_theta,thetas)
file_theta.close()

file_Dtheta=open("Dtheta.txt","w+")
np.savetxt(file_Dtheta,Dthetas)
file_Dtheta.close()

file_avr_activity=open("avr_activity.txt","w+")
np.savetxt(file_avr_activity,average_activity)
file_avr_activity.close()

file_theta_stim=open("theta_stim.txt","w+")
np.savetxt(file_theta_stim,thetas_stim)
file_theta_stim.close()

file_Dtheta_stim=open("Dtheta_stim.txt","w+")
np.savetxt(file_Dtheta_stim,Dthetas_stim)
file_Dtheta_stim.close()

file_avr_activity_stim=open("avr_activity_stim.txt","w+")
np.savetxt(file_avr_activity_stim,average_activity_stim)
file_avr_activity_stim.close()
