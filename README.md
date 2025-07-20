# Orbit Visualizer

Python tool for visualizing satellite orbits around Earth with dual-view plots.

🚀 **[Try the live web app here!](https://orbit-visualizer-gznudmagi3xloqsz6boyfp.streamlit.app/)**

## Features

- Interactive orbital parameter input (semi-major axis, eccentricity, true anomaly, inclination)
- Top view: orbital path visualization
- Side view: inclination relative to equatorial plane
- Real-time satellite position display

## Installation

```bash
pip install numpy matplotlib plotly streamlit
```

## Usage

**Web App**: [Live Streamlit app](https://orbit-visualizer-gznudmagi3xloqsz6boyfp.streamlit.app/)

**Python Module**:
```python
from Orbit_plotter import plot_orbit
plot_orbit(a=7000, e=0.1, v=1.5, i=45)
```

**Jupyter Notebook**: Run `main.ipynb` cells sequentially

## Parameters

- **a**: Semi-major axis (km)
- **e**: Eccentricity (0 ≤ e < 1)
- **v**: True anomaly (radians)  
- **i**: Inclination (degrees)

## Orbital Equation

```
r = a(1-e²)/(1+e·cos(v))
```

## Example (LEO)
- a = 7000 km, e = 0.01, v = 1.0, i = 60°

## Files

```
├── main.ipynb          # Interactive notebook
├── Orbit_plotter.py    # Core plotting function
├── main.py            # Main script
└── requirements.txt   # Dependencies
```

## License

MIT License - Created by Vinayak2005917
