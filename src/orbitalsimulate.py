import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
MU = 3.986004418e14  # Earth's gravitational parameter (m^3/s^2)
R_EARTH = 6371000    # Earth's mean radius (meters)

def orbit_equations(state, t):
    x, y, z, vx, vy, vz = state
    r = np.sqrt(x**2 + y**2 + z**2)
    ax = -MU * x / r**3
    ay = -MU * y / r**3
    az = -MU * z / r**3
    return [vx, vy, vz, ax, ay, az]

# Initial conditions (Altitude: 500 km)
altitude = 500000  # meters
r0 = R_EARTH + altitude
v0 = np.sqrt(MU / r0)  # Circular orbit velocity

inclination = np.radians(51.6) 
state0 = [r0, 0, 0, 0, v0 * np.cos(inclination), v0 * np.sin(inclination)]
t = np.linspace(0, 10800, 1000) 
sol = odeint(orbit_equations, state0, t)

x_orbit, y_orbit, z_orbit = sol[:, 0], sol[:, 1], sol[:, 2]

# Plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Draw Earth (a simple sphere)
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
x_earth = R_EARTH * np.cos(u) * np.sin(v)
y_earth = R_EARTH * np.sin(u) * np.sin(v)
z_earth = R_EARTH * np.cos(v)
ax.plot_wireframe(x_earth, y_earth, z_earth, color="blue", alpha=0.15, label="Earth")

# Plot the Satellite Orbit
ax.plot(x_orbit, y_orbit, z_orbit, color="red", linewidth=2.5, label="Satellite Path")

# Mark the starting point
ax.scatter(x_orbit[0], y_orbit[0], z_orbit[0], color="green", s=150, edgecolor='black', label="Start", zorder=5)

# Formatting
ax.set_xlabel('X (meters)', fontsize=12)
ax.set_ylabel('Y (meters)', fontsize=12)
ax.set_zlabel('Z (meters)', fontsize=12)
ax.set_title('3D Satellite Orbit Simulation - STAR.VISION Project', fontsize=14, fontweight='bold')
ax.legend(fontsize=12)

# Equalize axes
max_range = r0 * 1.1
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(-max_range, max_range)

# Adjust viewing angle for better 3D perception
ax.view_init(elev=25, azim=45)

plt.tight_layout()
output_path = '/mnt/data/orbit_3d_simulation.png'
plt.savefig(output_path, dpi=300)
print(f"Image saved successfully at {output_path}")
