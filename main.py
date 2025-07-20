import streamlit as st
import os
import Orbit_plotter as op
import time
from math import ceil, floor

#deleting older plot image if it exists
if os.path.exists("orbit_plot.png"):
    os.remove("orbit_plot.png")

st.title('Orbit Visualizer')

#taking user input for semi major axis, eccentricity, True anomaly and inclination
st.sidebar.header('Input Keplerian Parameters')
semi_major_axis = st.sidebar.number_input('Semi Major Axis (in km)', min_value=7000, max_value=1000000, value=10000)
eccentricity = st.sidebar.number_input('Eccentricity', min_value=0.0, max_value=1.0, value=0.1)
true_anomaly = st.sidebar.number_input('True Anomaly (in radians)', min_value=0.0, max_value=6.28, value=1.0)
inclination = st.sidebar.number_input('Inclination (in degrees)', min_value=0.0, max_value=360.0, value=25.0)


semi_major_axis = float(semi_major_axis)
eccentricity = float(eccentricity)
true_anomaly = float(true_anomaly)
inclination = float(inclination)
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