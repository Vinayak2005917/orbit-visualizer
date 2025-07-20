import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation


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
    plt.close()  # Close the figure to prevent memory issues

def plot_animated_orbit(a, e, i):
    lim = a*1.5
    if e > 0.45:
        lim = a*2
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))

    # Draw Earth once on both axes
    earth1 = patches.Circle((0, 0), radius=6378, color='blue', fill=True)
    earth2 = patches.Circle((0, 0), radius=6378, color='blue', fill=True)
    ax1.add_patch(earth1)
    ax2.add_patch(earth2)

    # Static orbit plot for top view
    v_range = np.linspace(0, 2*np.pi, 500)
    r = (a*(1 - e**2)) / (1 + e * np.cos(v_range))
    x_orbit = r * np.cos(v_range)
    y_orbit = r * np.sin(v_range)
    orbit_line, = ax1.plot(x_orbit, y_orbit, color='black', label='Orbit')

    # Initialize satellite point in top view
    satellite_dot, = ax1.plot([], [], 'ro', label='Satellite')
    
    # Add text to display true anomaly value
    anomaly_text = ax1.text(0.02, 0.98, '', transform=ax1.transAxes, fontsize=12,
                           verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Equatorial and orbital plane lines for side view
    equatorial_line, = ax2.plot([], [], color='black', linewidth=2, label='Equatorial plane')
    orbital_plane_line, = ax2.plot([], [], color='red', linewidth=3, label='Orbital plane')

    # Setup axes limits and labels
    for ax in (ax1, ax2):
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.legend()

    ax1.set_title("Top View - Satellite Orbit")
    ax1.set_xlabel('X (km)')
    ax1.set_ylabel('Z (km)')

    ax2.set_title("Side View - Satellite Orbit")
    ax2.set_xlabel('X (km)')
    ax2.set_ylabel('Y (km)')

    # Prepare side view static lines
    length = lim
    equatorial_line.set_data([-length, length], [0, 0])  # equatorial plane y=0

    # Calculate orbital plane line endpoints in side view
    angle_rad = np.deg2rad(i)
    perigee = a * (1 - e)
    apogee = a * (1 + e)
    x_orb = [ -apogee * np.cos(angle_rad), perigee * np.cos(angle_rad) ]
    y_orb = [ -apogee * np.sin(angle_rad), perigee * np.sin(angle_rad) ]
    orbital_plane_line.set_data(x_orb, y_orb)

    # Update function for animation
    v0 = 0
    def update(frame):
        true_anomaly = v0 + frame * 0.0628  # 0.0628 = 2*pi/100 for full orbit
        r = (a*(1 - e**2)) / (1 + e * np.cos(true_anomaly))
        x = r * np.cos(true_anomaly)
        y = r * np.sin(true_anomaly)

        satellite_dot.set_data([x], [y])
        
        # Update the text with current true anomaly value
        anomaly_text.set_text(f'True Anomaly: {true_anomaly:.2f} rad\n({true_anomaly * 57.3:.1f}°)')

        return satellite_dot, anomaly_text

    ani = FuncAnimation(fig, update, frames=100, interval=100, blit=True)

    plt.tight_layout()
    ani.save('orbit_animation.gif', writer='pillow', fps=15)
    plt.close()  # Close the figure after saving
    return ani  # Return the animation object