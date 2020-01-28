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
    
np.random.seed(3) 
  
K=.5
Nosc=60
dt = .1

theta0 = np.random.uniform(0.0,2.0*pi,Nosc)
omega0 = np.random.uniform(0.0,1.0,Nosc)

theta=theta0
DthetaDt=np.zeros(Nosc)
thetas=[]
Dthetas=[]
average_activity=[]
for t in range(200):
    DthetaDt = derives(Nosc,K,theta,omega0)
    theta=integrate_one_step(theta,DthetaDt,dt)
    # np.savetxt(file_theta,(theta[0],theta[1],theta[2]),fmt='%1.4e')
    time_theta=np.insert(theta,0,t*dt)
    time_Dtheta=np.insert(DthetaDt,0,t*dt)
    time_avr_activity = func_average_activity(Nosc,theta)
    average_activity.append(time_avr_activity)
    thetas.append(time_theta)
    Dthetas.append(time_Dtheta)

file_theta=open("theta.txt","w+")
np.savetxt(file_theta,thetas)
file_theta.close()

file_Dtheta=open("Dtheta.txt","w+")
np.savetxt(file_Dtheta,Dthetas)
file_Dtheta.close()

file_avr_activity=open("avr_activity.txt","w+")
np.savetxt(file_avr_activity,average_activity)
file_avr_activity.close()
