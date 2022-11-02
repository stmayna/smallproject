# %%
import numpy as np
import matplotlib.pyplot as plt
import random

# Water Temperature
T = float(input('What is the water Temperature? '))
if T > 24:
    print('Great, jump in!')
elif 20 <= T <= 24:
    print('Not bad. Put your toe in first!')
else:
    print('Do not swin. Too cold!')

# Finding The Maximum Height
v0 = 9
g = 9.81
t = np.linspace(0, 1, 1000)
y = v0*t - 0.5*g*t**2

largest_height = y[0]
for i in range(1, len(y), 1):
    if y[i] > largest_height:
        largest_height = y [i]

print('The largest height achieved was {:g} m'.format(largest_height))

# %%
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Heigt (m)')
plt.show()

# Random Walk In Two Dimensions
N = 1000                   # number of steps
d = 1                      # step length (e.g., in meter)
x = np.zeros(N+1)          # x coordinates 
y = np.zeros(N+1)          # y coordinates
x[0] = 0
y[0] = 0        # set initial position

for i in range(0, N, 1):
    r = random.random()         # random number in [0,1)
    if 0 <= r < 0.25:           # move north
        y[i+1] = y[i] + d
        x[i+1] = x[i]
    elif 0.25 <= r < 0.5:       # move east
        x[i+1] = x[i] + d
        y[i+1] = y[i]
    elif 0.5 <= r < 0.75:       # move south
        y[i+1] = y[i] - d
        x[i+1] = x[i]
    else:                       # move west
        x[i+1] = x[i] - d
        y[i+1] = y[i]

# %%
# plot path (mark start and stop with blue o and *, respectively)
plt.plot(x, y, 'r--', x[0], y[0], 'bo', x[-1], y[-1], 'b*')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# %%
