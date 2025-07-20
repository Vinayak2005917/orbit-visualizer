# Orbit Visualizer

Python tool for visualizing satellite orbits around Earth with dual-view plots and animations.

🚀 **[Try the live web app here!](https://orbit-visualizer-cuiqjpnmqbgzducbrmjdfm.streamlit.app/)**

## Features

- Interactive orbital parameter input (semi-major axis, eccentricity, true anomaly, inclination)
- **Static plots**: Top view orbital path and side view inclination visualization
- **Animated GIF**: Real-time satellite motion with true anomaly counter
- Real-time satellite position display with orbital parameters
- Earth representation with realistic radius (6378 km)
- Apogee and perigee distance calculations

## Installation

```bash
pip install numpy matplotlib streamlit
```

## Usage

**Web App**: [Live Streamlit app](https://orbit-visualizer-gznudmagi3xloqsz6boyfp.streamlit.app/) - No installation required!

**Python Module**:
```python
from Orbit_plotter import plot_orbit, plot_animated_orbit
plot_orbit(a=7000, e=0.1, v=1.5, i=45)
plot_animated_orbit(a=7000, e=0.1, i=45)  # Creates GIF animation
```

**Jupyter Notebook**: Run `main.ipynb` cells sequentially

## Parameters

- **a**: Semi-major axis (km) - Size of orbit
- **e**: Eccentricity (0 ≤ e < 1) - Shape of orbit (0=circular, >0=elliptical)
- **v**: True anomaly (radians) - Satellite position in orbit
- **i**: Inclination (degrees) - Orbital tilt relative to equator

## Features

### Static Visualization
- Dual-view plots (top and side perspectives)
- Shows current satellite position based on true anomaly
- Displays apogee and perigee distances
- Orbital and equatorial plane visualization

### Animated Visualization  
- Full orbital motion GIF generation
- Real-time true anomaly display in animation
- Distance from Earth center tracking
- Synchronized timing with orbital mechanics

## Orbital Equation

```
r = a(1-e²)/(1+e·cos(v))
```

## Example (ISS-like orbit)
- a = 6800 km, e = 0.01, v = 1.0, i = 51.6°

## Files

```
├── main.py             # Streamlit web application
├── main.ipynb          # Interactive Jupyter notebook  
├── Orbit_plotter.py    # Core plotting functions
└── README.md           # This documentation
```

## License

MIT License - Created by Vinayak2005917
