import streamlit as st
import os
import Orbit_plotter as op
import time
from math import ceil, floor

#deleting older plot image if it exists
if os.path.exists("orbit_plot.png"):
    os.remove("orbit_plot.png")

st.title('Orbit Visualizer')
st.write("Visualize satellite orbits around Earth with dual-view plots and animations. Either enter custom parameters or select from presets to quickly generate the orbit plots.")

#taking user input for semi major axis, eccentricity, True anomaly and inclination

mode = st.sidebar.toggle("Switch Paramter Type")

# Default to Keplerian parameters
if not mode:
    st.sidebar.header('Input simplified Parameters')
    apogee = float(st.sidebar.number_input('Apogee from sea level (in km)', min_value=0, max_value=1000000, value=500)) + 6378  # Adding Earth's radius
    perigee = float(st.sidebar.number_input('Perigee from sea level (in km)', min_value=0, max_value=1000000, value=500)) + 6378  # Adding Earth's radius
    inclination = float(st.sidebar.number_input('Inclination (in degrees)', min_value=0.0, max_value=360.0, value=25.0))
    # Convert simplified parameters to Keplerian elements
    semi_major_axis = (apogee + perigee) / 2
    eccentricity = (apogee - perigee) / (apogee + perigee)
    true_anomaly = 1  # Default value
    inclination = float(inclination)
else:
    # Default: Keplerian parameters (shows by default or when button 'a' is clicked)
    st.sidebar.header('Input Keplerian Parameters')
    semi_major_axis = float(st.sidebar.number_input('Semi Major Axis (in km)', min_value=7000, max_value=1000000, value=10000))
    eccentricity = float(st.sidebar.number_input('Eccentricity', min_value=0.0, max_value=1.0, value=0.1))
    true_anomaly = float(st.sidebar.number_input('True Anomaly (in radians)', min_value=0.0, max_value=6.28, value=1.0))
    inclination = float(st.sidebar.number_input('Inclination (in degrees)', min_value=0.0, max_value=360.0, value=25.0))


preset = st.sidebar.selectbox("Presets", options=["None","ISS", "SSO", "GEO", "GSO", "Molniya", "Tundra", "MEO", "Moon"], index=0, key="view_option")

if preset == "None":
    pass
elif preset == "ISS":
    semi_major_axis = 6780  # km
    eccentricity = 0.0007
    inclination = 51.6  # degrees
elif preset == "SSO":
    semi_major_axis = 7078  # km
    eccentricity = 0.0001
    inclination = 98.7  # degrees
elif preset == "GEO":
    semi_major_axis = 42164  # km
    eccentricity = 0.0001
    inclination = 0.0  # degrees
elif preset == "GSO":
    semi_major_axis = 42164
    eccentricity = 0.0001
    inclination = 0.0
elif preset == "Molniya":
    semi_major_axis = 26500
    eccentricity = 0.74
    inclination = 63.4
elif preset == "Tundra":
    semi_major_axis = 42164
    eccentricity = 0.1
    inclination = 63.4
elif preset == "MEO":
    semi_major_axis = 20000
    eccentricity = 0.1
    inclination = 55.0
elif preset == "Moon":
    semi_major_axis = 384400
    eccentricity = 0.0549
    inclination = 5.145

fig = op.plot_orbit(semi_major_axis, eccentricity, true_anomaly, inclination)

#button to plot animated orbit
st.sidebar.write("Generating animation takes some time, please be patient.")
if st.sidebar.button('Animate!'):
    # Delete old animation if it exists
    if os.path.exists("orbit_animation.gif"):
        os.remove("orbit_animation.gif")
    # Check if animation already exists
    if os.path.exists("orbit_animation.gif"):
        st.image("orbit_animation.gif", caption='Animated Orbit Plot')
        st.info("Using existing animation (click again to regenerate)")
    else:
        with st.spinner('Generating animation... This may take a moment.'):
            op.plot_animated_orbit(semi_major_axis, eccentricity, inclination)
        
        # Check if the GIF was created successfully
        if os.path.exists("orbit_animation.gif"):
            st.image("orbit_animation.gif", caption='Animated Orbit Plot')
            st.success("Animation generated successfully!")
        else:
            st.error("Failed to generate animation. Please try again.")
    st.sidebar.button('Static Plot', on_click=op.plot_orbit, args=(semi_major_axis, eccentricity, true_anomaly, inclination))

else:
    #Show static plot by default
    if os.path.exists("orbit_plot.png"):
        st.image("orbit_plot.png", caption='Static Orbit Plot')



st.write("### Orbit Parameters")
st.write(f"**Apogee:** {ceil(semi_major_axis * (1 + eccentricity)):.2f} km")
st.write(f"**Perigee:** {ceil(semi_major_axis * (1 - eccentricity)):.2f} km")