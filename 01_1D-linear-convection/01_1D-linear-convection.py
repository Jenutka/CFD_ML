import numpy as np
import matplotlib.pyplot as plt
import time,sys


# input values

nx=80       #number of grid points
dx=4/(nx-1) #distance between adjacent points
dt=0.025    #time of each timestep
nt=2       #number of timesteps
c=1         #wave speed

# initial conditions

u = np.zeros(nx) + 1    # setting the grid of zeros plus init value
u[int(0.5/dx):int(1/dx+1)] = 2 # setting interval 0.5-1 to value 2
uinit = np.zeros(nx) + 1    # setting the grid of zeros plus init value
uinit[int(0.5/dx):int(1/dx+1)] = 2 # setting interval 0.5-1 to value 2
print(u)
print(np.linspace(0,2,nx), u)

# Plot visualizing

plt.style.use('dark_background')
fig, axis = plt.subplots()
axis.plot(np.linspace(0,2,nx), u)
axis.set(xlabel="x direction", ylabel="u", title="1D linear convection")
axis.grid()

# discretization & simulation

counter = 0

while counter < nt:
    un = np.zeros(nx) + 1   # variable to store value of previous time step
    un = u.copy()      # copy existing values of u
    for i in range(1,nx):
        u[i] = un[i] - c * (dt/dx) * (un[i] - un[i-1])
    counter += dt
    print(counter, np.average(u))

    # plot update
    axis.clear()
    axis.plot(np.linspace(0,2,nx), uinit, label='initial shape')
    axis.plot(np.linspace(0,2,nx), u, label='simulated shape after n-timesteps')
    axis.set(xlabel="x direction", ylabel="u", title="1D linear convection")
    plt.legend()
    plt.pause(0.01)

plt.show()
