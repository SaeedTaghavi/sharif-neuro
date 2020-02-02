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



K=.4
Nosc=1000
dt = 0.1
np.random.seed(3) 

theta0 = np.random.uniform(0.0,2.0*pi,Nosc)
#omega0 = np.random.uniform(0.9,1.0,Nosc)
omega0 = np.random.normal(1.0, 0.1, Nosc)

#it_stim=196
for it_stim in range(630,640):
    print (it_stim)
    print ("......")

    theta_stim=theta0
    DthetaDt_stim=np.zeros(Nosc)
    thetas_stim=[]
    Dthetas_stim=[]
    average_activity_stim=[]
    r_prev_stim,psi_prev_stim=calc_order_param(Nosc,theta0)

    for t in range(1000):
        DthetaDt_stim = derives(Nosc,K,theta_stim,omega0)
        r_stim, psi_stim = calc_order_param(Nosc,theta_stim)
        if (t==it_stim):
            DthetaDt_stim = DthetaDt_stim - 5.*np.sin(theta_stim)
    #    if (abs( np.cos(psi)+ 0.7 )<0.01):
    #        if (np.cos(psi)<np.cos(psi_prev)):
    #            DthetaDt = DthetaDt - 5.*np.sin(theta)
    #    if ( np.cos(psi)<- 0.8):
    #        if (np.cos(psi_prev)>-0.8):
    #            DthetaDt = DthetaDt - 5.*np.sin(theta)

    #    psi_prev=psi; r_prev=r

        theta_stim=integrate_one_step(theta_stim,DthetaDt_stim,dt)
        time_theta_stim=np.insert(theta_stim,0,t*dt)
        time_Dtheta_stim=np.insert(DthetaDt_stim,0,t*dt)
        time_avr_activity_stim = func_average_activity(Nosc,theta_stim)
        average_activity_stim.append(time_avr_activity_stim)
        thetas_stim.append(time_theta_stim)
        Dthetas_stim.append(time_Dtheta_stim)

    filename='theta_tp={:08.4}'.format(it_stim*dt)
    extension="_.txt"
    filename=filename+extension
    file_theta_stim=open(filename,"w+")
    np.savetxt(file_theta_stim,thetas_stim)
    file_theta_stim.close()

    filename='DthetaDt_tp={:08.4}'.format(it_stim*dt)
    extension="_.txt"
    filename=filename+extension
    file_Dtheta_stim=open(filename,"w+")
    np.savetxt(file_Dtheta_stim,Dthetas_stim)
    file_Dtheta_stim.close()

    filename='AvrActivity_tp={:08.4}'.format(it_stim*dt)
    extension="_.txt"
    filename=filename+extension
    file_avr_activity_stim=open(filename,"w+")
    np.savetxt(file_avr_activity_stim,average_activity_stim)
    file_avr_activity_stim.close()
    print (it_stim," done!")
