import matplotlib.pyplot as plt
import numpy as np
from math import pi
N=1000
x=np.linspace(0.,15.,N)
y1=np.sin(.17*pi*x+pi/4.)
y2=np.sin(3.0*pi*x)
y=y1*y2
stim_amp=np.zeros(N)
stim_phase=np.zeros(N)
lock_phase=3*pi/2.0
amp_thershold=0.7
for i in range(N):
	if (abs(y1[i]) > amp_thershold ):
		if (stim_amp[i-1]==0.0):
			stim_amp[i]=1.0
for i in range(N):
	if (i<990):
		if (stim_amp[i]==1.0):
			for j in range(1,10):
				stim_amp[i+j]=0.0

#for i in range(N):
#	if ( abs( y2[i] - np.sin(lock_phase) ) <.1 and y2[i]>y2[i-1] ):
#		if (stim_phase[i-1]==0.0):
#			stim_phase[i]=1.0
for i in range(1,N):
	if (y[i-1]<y[i]>y[i+1]):
		stim_phase[i]=1.0

plt.figure(1)
plt.subplot(211)
plt.plot(x,y)
plt.hlines(amp_thershold,x[0],x[-1])
plt.xticks([])
plt.yticks([])
#plt.xlabel('Time')
plt.ylabel('Oscillationg Parameter')

plt.subplot(212)
plt.plot(x,stim_amp)
plt.xticks([])
plt.yticks([])
plt.xlabel('Time')
plt.ylabel('Trigger')
plt.savefig('adaptive-dbs.png')

plt.figure(2)
plt.subplot(211)
plt.plot(x,y)
plt.xticks([])
plt.yticks([])

#plt.xlabel('Time')
plt.ylabel('Oscillationg Parameter')

plt.subplot(212)
plt.plot(x,stim_phase)
plt.xticks([])
plt.yticks([])
plt.xlabel('Time')
plt.ylabel('Trigger')
plt.savefig('phase-locked-dbs.png')


label_font_size=30

plt.figure(figsize=(15,12))
plt.subplot(311)
plt.plot(x,y)
plt.hlines(amp_thershold,x[0],x[-1])
plt.xticks([])
plt.yticks([])
#plt.xlabel('Time')
#plt.ylabel('Oscillating Parameter',fontsize=label_font_size)
plt.ylabel('Activity',fontsize=label_font_size)

plt.subplot(312)
plt.plot(x,stim_amp)
plt.xticks([])
plt.yticks([])
plt.ylabel('Adaptive DBS',fontsize=label_font_size)


plt.subplot(313)
plt.plot(x,stim_phase)
plt.xticks([])
plt.yticks([])
plt.xlabel('Time',fontsize=label_font_size)
plt.ylabel(r'Phase-locked DBS',fontsize=label_font_size-5)

plt.savefig('all.png')
#plt.show()

