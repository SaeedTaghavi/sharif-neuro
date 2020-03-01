import numpy as np
from math import pi
import matplotlib.pyplot as plt

def mu(y, t): 
    """Implement the Ornstein–Uhlenbeck mu.""" ## = \theta (\mu-Y_t)
    return c_theta * (c_mu - y)

def sigma(y, t): 
    """Implement the Ornstein–Uhlenbeck sigma.""" ## = \sigma
    return c_sigma
    
def dW(delta_t): 
    """Sample a random number at each call."""
    return np.random.normal(loc = 0.0, scale = np.sqrt(delta_t))



num_sims = 1  ### display num_sims runs

t_init = 0.0
t_end  = 10.0
N      = 1000 ### Compute 1000 grid points
dt     = float((t_end - t_init) / N )

Nosc   = 3
theta0 = np.random.uniform( low = 0.0, high = 2.0*pi, size = Nosc )
y_init = theta0

ts     = np.arange(t_init, t_end, dt)

ys1    = np.zeros(N)
ys2    = np.zeros(N)

ys1[0] = y_init
ys2[0] = y_init+2.

for isim in range(num_sims):
    np.random.seed(isim) 
    for i in range(1, ts.size):
        t = (i-1) * dt
        y1 = ys1[i-1]
        ys1[i] = y1 + mu(y1, t) * dt + sigma(y1, t) * dW(dt)
        y2 = ys2[i-1]
        ys2[i] = y2 + mu(y2, t) * dt + sigma(y2, t) * dW(dt)
    plt.plot(ts, ys1)
    plt.plot(ts, ys2)
plt.show()
