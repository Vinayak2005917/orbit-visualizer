# Orbit Visualizer

Python tool for visualizing satellite orbits around Earth with dual-view plots and animations.

🚀 **[Try the live web app here!](https://orbit-visualizer-cuiqjpnmqbgzducbrmjdfm.streamlit.app/)**

## Screenshots

### Static Visualization
![Static Orbit Plot](Screenshots/Screenshot%202025-07-21%20004231.png)
*Dual-view orbital visualization showing top and side perspectives*

### Animated Visualization  
![Animation Example](Screenshots/Screenshot%202025-07-21%20004620.png)
*Real-time animated orbit with true anomaly counter*

### Parameter Input Options
![Parameter Interface](Screenshots/Screenshot%202025-07-21%20004648.png)
*Toggle between Keplerian and simplified parameters*

### Orbital Presets
![Preset Options](Screenshots/Screenshot%202025-07-21%20004707.png)
*Quick access to common orbital configurations*

## Features

- **Dual Parameter Input Modes**:
  - Keplerian parameters (semi-major axis, eccentricity, true anomaly, inclination)
  - Simplified parameters (apogee/perigee heights from sea level)
- **Orbital Presets**: ISS, Sun-Synchronous, GEO, Molniya, Tundra, MEO, Moon orbit
- **Static plots**: Top view orbital path and side view inclination visualization
- **Animated GIF**: Real-time satellite motion with true anomaly and distance display
- **Real-time calculations**: Apogee and perigee distances
- **Earth representation**: Realistic radius (6378 km) and visual scaling

## Installation

```bash
pip install numpy matplotlib streamlit
```

## Usage

**Web App**: [Live Streamlit app](https://orbit-visualizer-cuiqjpnmqbgzducbrmjdfm.streamlit.app/) - No installation required!

**Python Module**:
```python
from Orbit_plotter import plot_orbit, plot_animated_orbit
plot_orbit(a=7000, e=0.1, v=1.5, i=45)
plot_animated_orbit(a=7000, e=0.1, i=45)  # Creates GIF animation
```

**Jupyter Notebook**: Run `main.ipynb` cells sequentially

## Parameters

### Keplerian Elements (Advanced)
- **a**: Semi-major axis (km) - Size of orbit
- **e**: Eccentricity (0 ≤ e < 1) - Shape of orbit (0=circular, >0=elliptical)
- **v**: True anomaly (radians) - Satellite position in orbit
- **i**: Inclination (degrees) - Orbital tilt relative to equator

### Simplified Parameters (Beginner-friendly)
- **Apogee**: Highest altitude above sea level (km)
- **Perigee**: Lowest altitude above sea level (km)
- **Inclination**: Orbital tilt relative to equator (degrees)

## Orbital Presets

| Preset | Description | Altitude | Inclination |
|--------|-------------|----------|-------------|
| **ISS** | International Space Station | ~400 km | 51.6° |
| **SSO** | Sun-Synchronous Orbit | ~700 km | 98.7° |
| **GEO** | Geostationary Earth Orbit | 35,786 km | 0° |
| **Molniya** | Highly elliptical orbit | 500-39,000 km | 63.4° |
| **MEO** | Medium Earth Orbit | ~20,000 km | 55° |
| **Moon** | Lunar orbit | 384,400 km | 5.1° |

## Features in Detail

### Static Visualization
- Dual-view plots (top and side perspectives)
- Current satellite position based on true anomaly
- Orbital and equatorial plane visualization
- Automatic plot scaling based on orbit size

### Animated Visualization  
- Full orbital motion GIF generation
- Real-time true anomaly display in animation
- Distance from Earth center tracking
- Synchronized timing with orbital mechanics
- Text overlay showing orbital parameters

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
