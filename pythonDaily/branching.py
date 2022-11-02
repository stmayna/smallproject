# %%
import numpy as np
import matplotlib.pyplot as plt

# T = float(input('What is the water Temperature? '))
# if T > 24:
#     print('Great, jump in!')
# elif 20 <= T <= 24:
#     print('Not bad. Put your toe in first!')
# else:
#     print('Do not swin. Too cold!')

v0 = 4.5
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
# %%
