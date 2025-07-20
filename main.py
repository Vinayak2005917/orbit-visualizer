import streamlit as st
import os
import Orbit_plotter as op

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


#displaying an image in Streamlit
st.image("orbit_plot.png")
