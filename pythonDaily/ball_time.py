# %%
import numpy as np
import matplotlib.pyplot as plt

v0 = 4.5
g = 9.81
t = np.linspace(0, 1, 1000)
y = v0*t - 0.5*g*t**2

i = 0
while y[i] >= 0:
    i = i + 1

print('Time of flight (in seconds): {:g}'.format(t[i]))

# %%
plt.plot(t, y)
plt.plot(t, 0*t, 'g--')
plt.xlabel('Time (s)')
plt.ylabel('Heigt (m)')
plt.show()

# %%
