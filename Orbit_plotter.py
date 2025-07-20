import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot_orbit(a, e, v, i):
    v_range = np.linspace(0, 6.28, 200)
    r = (a*(1-(e**2)))/(1+e*np.cos(v_range))
    position = (a*(1-(e**2)))/(1+e*np.cos(v))
    lim = a*1.5
    if e > 0.45:
        lim = a*2

    # Converting from polar to Cartesian
    x = r * np.cos(v_range)
    y = r * np.sin(v_range)
    
    # Create figure and axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6)) 

    # First subplot - Top View
    ax1.set_title("Top View - Satellite Orbit")
    ax1.set_xlabel('X - axis')
    ax1.set_ylabel('Z - axis')
    ax1.grid(True)
    ax1.set_axisbelow(True)

    # Create a circle patch for Earth
    earth1 = patches.Circle((0, 0), radius=6378, color='blue', fill=True)
    ax1.add_patch(earth1)
    ax1.set_aspect('equal')
    ax1.set_xlim(-lim, lim)
    ax1.set_ylim(-lim, lim)

    # Plot the orbit
    ax1.plot(x, y, color="black", label='Orbit', zorder=1)

    # Plot the Satellite
    x_orbit = position * np.cos(v)
    y_orbit = position * np.sin(v)
    ax1.scatter(x_orbit, y_orbit, color='Red', label='Satellite')
    ax1.legend(loc='upper right')

    # Second subplot - Side View
    ax2.set_title('Side View - Satellite Orbit')
    ax2.set_xlabel('X - axis')
    ax2.set_ylabel('Y - axis')
    ax2.grid(True)

    earth2 = patches.Circle((0, 0), radius=6378, color='blue', fill=True)
    ax2.add_patch(earth2)
    ax2.set_aspect('equal')
    ax2.set_xlim(-lim, lim)
    ax2.set_ylim(-lim, lim)

    # Equatorial plane
    length = lim
    angle_rad = np.deg2rad(0)
    x1 = length * np.cos(angle_rad)
    y1 = length * np.sin(angle_rad)
    x2 = -length * np.cos(angle_rad)
    y2 = -length * np.sin(angle_rad)
    ax2.plot([x2, x1], [y2, y1], color='black', linewidth=2, label='Equatorial plane')

    # Orbital plane
    perigee = a*(1-e)
    apogee = a*(1+e)
    angle_rad = np.deg2rad(i)
    x1 = perigee * np.cos(angle_rad)
    y1 = perigee * np.sin(angle_rad)
    x2 = -apogee * np.cos(angle_rad)
    y2 = -apogee * np.sin(angle_rad)
    ax2.plot([x2, x1], [y2, y1], color='red', linewidth=3, label='Orbital plane')

    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig("orbit_plot.png")