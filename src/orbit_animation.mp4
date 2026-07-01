import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# orbit
theta = np.linspace(0, 2*np.pi, 500)
R_earth = 6371
orbit_r = R_earth + 500

x = orbit_r * np.cos(theta)
y = orbit_r * np.sin(theta)

# figure
fig, ax = plt.subplots(figsize=(7,7))

# earth
earth = plt.Circle((0,0), R_earth, color='blue', alpha=0.5, label='Earth')
ax.add_patch(earth)

# orbit path
ax.plot(x, y, 'gray', linestyle='--', label='Orbit Path')

# satellite point
satellite, = ax.plot([], [], 'ro', markersize=8, label='Satellite')

ax.set_xlim(-8000, 8000)
ax.set_ylim(-8000, 8000)
ax.set_aspect('equal')
ax.set_title("Satellite Orbit Animation")
ax.legend(loc='upper right')

# animation function
def update(frame):
    satellite.set_data([x[frame]], [y[frame]])
    return satellite,

ani = FuncAnimation(fig, update, frames=len(theta), interval=20, blit=True)

# Save as MP4
output_path = '/mnt/data/orbit_animation.mp4'
ani.save(output_path, writer='ffmpeg')
print(f"Animation saved successfully at {output_path}")
