import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np

#EX9
print("EX9")
x = np.array([-1.5, -1, 0.5, 0.5, 0.75, 0.75, 1, 1.5, 1, 1, 0, 0, -0.5, -0.5, -1, -1, -1.5])
y = np.array([1, 2, 2, 2.5, 2.5, 2, 2, 1, 1, 0, 0, 0.75, 0.75, 0, 0, 1, 1])
plt.plot(x, y, 'o-', label="Original")


plt.title('Transformed Circle Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

t_x, t_y = 2, 4
x_translated = x + t_x
y_translated = y + t_y
plt.plot(x_translated, y_translated, 'o-', label="Translated")
plt.show()

alpha = np.pi/3
R = np.array([[np.cos(alpha), -np.sin(alpha)],
              [np.sin(alpha), np.cos(alpha)]])
xy_rotated = np.vstack((x, y)).T.dot(R)

plt.title('Rotationed')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

x_rotated = xy_rotated[:, 0]
y_rotated = xy_rotated[:, 1]
plt.plot(x_rotated, y_rotated, 'o-', label="Rotated")
plt.show()

S_x, S_y = 2, 3
S = np.array([[S_x, 0],
              [0, S_y]])

xy_scaled = np.vstack((x, y)).T.dot(S)
x_scaled = xy_scaled[:, 0]
y_scaled = xy_scaled[:, 1]

plt.title('Scaled')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x_scaled, y_scaled, 'o-', label="Scaled")
plt.show()

# Shear
Shear_x = 0.5
Shear_y = -1.5

Sh_x = np.array([[1, Shear_x],
                 [0, 1]])
Sh_y = np.array([[1, 0],
                 [Shear_y, 1]])

xy_sheared_x = np.vstack((x, y)).T.dot(Sh_x)
x_sheared_x = xy_sheared_x[:, 0]
y_sheared_x = xy_sheared_x[:, 1]
plt.plot(x_sheared_x, y_sheared_x, 'o-', label="Sheared x")

xy_sheared_y = np.vstack((x, y)).T.dot(Sh_y)
x_sheared_y = xy_sheared_y[:, 0]
y_sheared_y = xy_sheared_y[:, 1]

plt.title('Shear')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x_sheared_y, y_sheared_y, 'o-', label="Sheared y")
plt.show()