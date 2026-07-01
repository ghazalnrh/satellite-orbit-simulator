import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Data
theta = np.linspace(0, 2*np.pi, 50) # Reduced frames for size/speed
R_earth = 6371
orbit_r = R_earth + 500
x = orbit_r * np.cos(theta)
y = orbit_r * np.sin(theta)

# Figure
fig, ax = plt.subplots(figsize=(7,7))
earth = plt.Circle((0,0), R_earth, color='blue', alpha=0.5)
ax.add_patch(earth)
ax.plot(x, y, 'gray', linestyle='--')
satellite, = ax.plot([], [], 'ro', markersize=8)

ax.set_xlim(-8000, 8000)
ax.set_ylim(-8000, 8000)
ax.set_aspect('equal')
ax.set_title("Satellite Orbit Animation")

def update(frame):
    satellite.set_data([x[frame]], [y[frame]])
    return satellite,

# Save as GIF
ani = FuncAnimation(fig, update, frames=len(theta), interval=100, blit=True)
output_path = '/mnt/data/orbit_animation.gif'
ani.save(output_path, writer=PillowWriter(fps=15))
print(f"GIF saved successfully at {output_path}")
