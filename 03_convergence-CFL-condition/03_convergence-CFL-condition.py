## Convergence, CFL-number condition ##

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time,sys


# input values

nx=61       #number of grid points
dx=2/(nx-1) #distance between adjacent points
nt=20       #number of timesteps
c=1         #wave speed
sigma=0.5   #CFL number

dt = sigma * dx

# initial conditions

u = np.zeros(nx) + 1    # setting the grid of zeros plus init value
u[int(0.5/dx):int(1/dx+1)] = 2 # setting interval 0.5-1 to value 2
uinit = np.zeros(nx) + 1    # setting the grid of zeros plus init value
uinit[int(0.5/dx):int(1/dx+1)] = 2 # setting interval 0.5-1 to value 2
print(u)
print(np.linspace(0,2,nx), u)

# Plot visualizing

parameter_title = ("1D linear convection, " + "nr. of grid points = " + str(nx) + 
                   ", timestep dt = " + str(round(dt, 3)))

#plt.style.use('dark_background')
fig, axis = plt.subplots()
axis.set(xlabel="x direction", ylabel="u", title="1D linear convection")
axis.grid()

# discretization & simulation

un = np.zeros(nx) + 1   # variable to store value of previous time step


def animate(i):

    un = u.copy()      # copy existing values of u
    for n in range(1,nx):
        u[n] = un[n] - c * (dt/dx) * (un[n] - un[n-1])

    print(u) 

    # plot update
    axis.clear()
    init_line = axis.plot(np.linspace(0,2,nx), uinit, label='initial shape')
    n_line = axis.plot(np.linspace(0,2,nx), un, label='simulated shape after n-timesteps')
    axis.set(xlabel="x direction", ylabel="u", title=parameter_title)
    plt.legend(loc=3)
    return n_line

#plt.show()
ani = animation.FuncAnimation(fig, animate, interval=80, blit=False, 
                              repeat_delay=1000, repeat=True, frames=30)
ani.save('1D_lc_sigma_nx61.gif', dpi=100, writer=animation.PillowWriter(fps=25))
plt.show()
