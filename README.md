# Solar System Animation

An animated visualization of the solar system showing planets, dwarf planets, asteroids, moons, and comets.

## Files

- **SolarSystem.py** - Main animation script (~150 lines, loads from JSON)
- **celestial_bodies.json** - Database of all celestial body properties

## Running the Animation

```bash
python SolarSystem.py
```

## Design Benefits

### Clean Architecture
- **Concise**: ~150 lines of clean, reusable code
- **Data-Driven**: All orbital parameters stored in JSON
- **Maintainable**: Single animation function handles all bodies

### Easy Modifications
- **Update Parameters**: Change orbital values in JSON without touching code
- **Add Bodies**: Add new planets/moons by simply adding JSON entries
- **Clear Structure**: Hierarchical organization (planets have moons)

### Example: Adding a New Moon

Just add to the JSON:
```json
"Titan": {
  "radP": 0.00793,
  "radA": 0.00840,
  "rad": 0.00816,
  "frames": 16,
  "eccentricity": 0.0288,
  "color": "red",
  "lineColor": "orange",
  "markerSize": 3
}
```

## Celestial Bodies Included

### Planets
- Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

### Dwarf Planets
- Pluto, Haumea, Makemake

### Asteroids
- Vesta, Ceres

### Moons
- Earth: Moon
- Mars: Phobos, Deimos
- Jupiter: Io, Europa, Ganymede, Callisto
- Saturn: Titan, Enceladus
- Uranus: Miranda
- Neptune: Triton

### Comets
- Halley's Comet

## Data Structure

The JSON file organizes data hierarchically:
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
      "moons": {
        "Moon": { ... }
      }
    }
  }
}
```

## Requirements

- Python 3.x
- matplotlib
- numpy

Install dependencies:
```bash
pip install matplotlib numpy
```
