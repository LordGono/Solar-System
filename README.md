# 3D Solar System Animation

A stunning **3D interactive visualization** of the solar system showing real orbital inclinations for planets, dwarf planets, asteroids, moons, and comets.

## What's New in 3D

✨ **Real Orbital Inclinations** - See how planets are actually tilted relative to the ecliptic plane
- Pluto: 17.2° tilt
- Halley's Comet: 162.3° (wild retrograde orbit!)
- Triton: 156.8° (Neptune's backwards moon!)

🎮 **Interactive 3D Controls** - Fully rotate, zoom, and explore the solar system from any angle

📊 **Scientific Accuracy** - Based on real astronomical data from NASA/JPL

## Files

- **SolarSystem.py** - Main 3D animation script (~350 lines)
- **celestial_bodies.json** - Database of all celestial body properties including inclination data

## Running the Animation

```bash
python SolarSystem.py
```

The visualization will open in your default web browser with full 3D interactivity.

## Requirements

- Python 3.x
- plotly
- numpy

Install dependencies:
```bash
pip install plotly numpy
```

## Interactive Features

### Control Buttons

**Play/Pause Controls**
- `> Play` - Start the orbital animation
- `|| Pause` - Pause the animation

**Speed Controls**
- `0.5x` - Slow motion (half speed)
- `1x` - Normal speed
- `2x` - Double speed
- `5x` - Fast forward (5x speed)

**View Presets**
- `Top View` - Look down from above the solar system
- `Side View` - See inclinations from the side
- `Angled` - Default angled perspective (best for seeing 3D structure)

### Mouse Controls

- **Click + Drag** - Rotate the 3D view in any direction
- **Scroll Wheel** - Zoom in/out
- **Right-Click + Drag** - Pan the camera
- **Click Legend** - Show/hide specific celestial bodies

### Visual Features

- **3D Orbit Trails** - See the complete orbital paths in 3D space
- **Real-Time Labels** - Each body is labeled and follows its position
- **Color-Coded Bodies** - Easy identification by color
- **Hover Information** - See exact 3D coordinates (X, Y, Z in AU)
- **Dark Space Theme** - Beautiful background matching real space

## Celestial Bodies Included (26 Total)

### Star
- Sun (reference point at origin)

### Planets (8)
- Mercury (7.0° inclination)
- Venus (3.4°)
- Earth (0.0° - defines the ecliptic)
- Mars (1.85°)
- Jupiter (1.3°)
- Saturn (2.5°)
- Uranus (0.77°)
- Neptune (1.77°)

### Dwarf Planets (3)
- Pluto (17.2° - highly tilted!)
- Haumea (28.2°)
- Makemake (29.0°)

### Asteroids (2)
- Vesta (7.1°)
- Ceres (10.6°)

### Moons (10)
- **Earth**: Moon (5.1°)
- **Mars**: Phobos (1.1°), Deimos (1.8°)
- **Jupiter**: Io (0.04°), Europa (0.47°), Ganymede (0.21°), Callisto (0.51°)
- **Saturn**: Titan (0.34°), Enceladus (0.0°)
- **Uranus**: Miranda (4.2°)
- **Neptune**: Triton (156.8° - retrograde!)

### Comets (1)
- Halley's Comet (162.3° - extreme inclination!)

## Data Structure

The JSON file now includes inclination data for 3D positioning:

```json
{
  "simulation": {
    "Nframes": 365,
    "rad": 50,
    "tinterval": 1000
  },
  "bodies": {
    "Earth": {
      "type": "planet",
      "radP": 0.9832899,
      "radA": 1.0167103,
      "frames": 365,
      "eccentricity": 0.0167,
      "inclination": 0.0,
      "color": "blue",
      "markerSize": 4,
      "moons": {
        "Moon": {
          "inclination": 5.1,
          ...
        }
      }
    }
  }
}
```

## Technical Details

### 3D Coordinate System
- **X-axis**: Along ecliptic plane
- **Y-axis**: Along ecliptic plane (perpendicular to X)
- **Z-axis**: Perpendicular to ecliptic (where inclinations show up)
- **Units**: Astronomical Units (AU) - 1 AU = Earth-Sun distance

### Orbital Math
Inclinations are applied as rotations around the X-axis:
```python
y_inclined = y * cos(inclination)
z_inclined = y * sin(inclination)
```

### Moon Positioning
Moons orbit relative to their parent planet's position, inheriting the parent's location and adding their own orbital motion.

### Performance Optimization
- Animation limited to ~200 frames for smooth playback
- Efficient trajectory pre-calculation
- Optimized 3D rendering via Plotly

## Design Benefits

### Clean Architecture
- **Data-Driven**: All orbital parameters stored in JSON
- **Modular**: Separate trajectory generation and visualization
- **Maintainable**: Clear function separation and documentation
- **Interactive**: Built-in Plotly controls and animations

### Easy Modifications

**Add a new celestial body:**
Just add to the JSON with inclination data:
```json
"NewPlanet": {
  "type": "planet",
  "radP": 5.0,
  "radA": 5.2,
  "frames": 1000,
  "eccentricity": 0.05,
  "inclination": 12.5,
  "color": "purple",
  "markerSize": 4
}
```

**Add a moon to any planet:**
```json
"Jupiter": {
  "moons": {
    "NewMoon": {
      "radP": 0.01,
      "radA": 0.012,
      "frames": 30,
      "eccentricity": 0.02,
      "inclination": 2.0,
      "color": "white",
      "markerSize": 1
    }
  }
}
```

## Why 3D?

The 2D view was great, but it couldn't show one of the most important features of planetary orbits: **orbital inclination**. In 3D you can now see:

1. **How Pluto's orbit is wildly tilted** compared to the main planets
2. **Retrograde orbits** like Triton and Halley's Comet going "backwards"
3. **The ecliptic plane** as a reference (most planets are close to it)
4. **Moon inclinations** relative to their parent planets
5. **The actual 3D structure** of our solar system

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Tips for Best Experience

1. **Start with Top View** to see the classic 2D solar system view
2. **Switch to Side View** to see all the inclinations clearly
3. **Use Angled View** for the best 3D perspective
4. **Zoom in on Jupiter** to see the Galilean moons in detail
5. **Speed up to 5x** to see outer planets move faster
6. **Click legend items** to hide inner planets and focus on outer solar system

---

**Built with love using Plotly, NumPy, and real astronomical data** 🚀🌌
