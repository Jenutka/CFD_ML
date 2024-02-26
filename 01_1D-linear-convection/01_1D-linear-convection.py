import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

def animate(i):

    un = np.zeros(nx) + 1   # variable to store value of previous time step
    un = u.copy()      # copy existing values of u
    data = []
    for n in range(1,nx):
        u[n] = un[n] - c * (dt/dx) * (un[n] - un[n-1])
        data.append(u[n])

    print(data) 
    print(len(data))
    # plot update
    axis.clear()
    n_line = axis.plot(np.linspace(0,2,nx-1), data, label='simulated shape after n-timesteps')
    axis.set(xlabel="x direction", ylabel="u", title="1D linear convection")
    plt.legend()
    print(n_line)
    return n_line

#plt.show()
ani = animation.FuncAnimation(fig, animate, interval=40, blit=True, 
                              repeat=True, frames=10)
plt.show()
ani.save('1D_lc.gif', dpi=300, writer=animation.PillowWriter(fps=25))
