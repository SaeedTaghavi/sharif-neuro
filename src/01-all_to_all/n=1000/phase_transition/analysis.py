import matplotlib.pyplot as plt
import numpy as np
from math import pi

data=np.loadtxt('k-r.txt')
data = np.transpose(data)
plt.plot(data[0],data[1],'s-')
plt.xlabel(r"$k$",fontsize=18)
plt.ylabel(r"$r$",fontsize=18)
#plt.show()
plt.savefig("k-r.png")
exit()

