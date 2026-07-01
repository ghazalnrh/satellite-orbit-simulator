import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Earth Parameters
# -----------------------------
R_earth = 6371  # km
mu = 398600     # km^3/s^2

# -----------------------------
# Orbit Parameters
# -----------------------------
altitude = 500  # km
r = R_earth + altitude

# circular orbit velocity
v = np.sqrt(mu / r)

# orbital period
T = 2 * np.pi * np.sqrt(r**3 / mu)

# simulation time
t = np.linspace(0, T, 1000)

# -----------------------------
# Satellite Position
# -----------------------------
theta = 2 * np.pi * t / T

x = r * np.cos(theta)
y = r * np.sin(theta)

# -----------------------------
# Convert to Latitude/Longitude
# -----------------------------
lat = np.degrees(np.arcsin(y / r))
lon = np.degrees(np.arctan2(y, x))

# -----------------------------
# Plot Ground Track
# -----------------------------
plt.figure(figsize=(12,6))
plt.plot(lon, lat, 'r', linewidth=2)

plt.title("Satellite Ground Track")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.xlim(-180, 180)
plt.ylim(-90, 90)

plt.grid(True)
plt.show()