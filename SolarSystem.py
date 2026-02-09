import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

# Load celestial bodies data from JSON
with open('celestial_bodies.json', 'r') as f:
    data = json.load(f)

# Extract simulation parameters
sim = data['simulation']
Nframes = sim['Nframes']
rad = sim['rad']
tinterval = sim['tinterval']

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot2grid((3, 3), (0, 0), colspan=10, rowspan=10,
                       xlim=(-2.*rad, 2.*rad), ylim=(-2.*rad, 2.*rad), aspect='equal')
ax.set_adjustable('box')
ax.grid(False)
ax.axis('off')

# Store animation objects and data
animations = []
bodies_data = {}

def create_body_animation(name, body_props, parent_name=None):
    """Create animation for a celestial body (planet, moon, etc.)"""
    # Extract properties
    radP = body_props['radP']
    radA = body_props['radA']
    frames = body_props['frames']
    ecc = body_props['eccentricity']
    color = body_props['color']
    line_color = body_props.get('lineColor', color)
    marker_size = body_props['markerSize']

    # Create orbit circle (cosmetic)
    orbit_radius = body_props['rad']
    if orbit_radius > 0:
        orbit_circle = plt.Circle((0, 0), radius=orbit_radius,
                                  facecolor="None", edgecolor="k", lw=1)
        ax.add_patch(orbit_circle)

    # Create plot elements
    body_marker, = ax.plot([], [], marker='o', ms=marker_size, color=color)
    body_line, = ax.plot([], [], lw=1, color=line_color)

    # Data storage
    xdata = []
    ydata = []

    # Store in global dict
    bodies_data[name] = {
        'marker': body_marker,
        'line': body_line,
        'xdata': xdata,
        'ydata': ydata,
        'props': body_props,
        'parent': parent_name
    }

    # Init function
    def init():
        body_marker.set_data([], [])
        body_line.set_data([], [])
        return body_marker, body_line

    # Animation function
    def animate(i):
        t = 2. * np.pi * float(i / (frames - 1.))

        # Calculate position
        if parent_name and parent_name in bodies_data:
            # Moon orbiting a planet
            parent_data = bodies_data[parent_name]
            parent_props = parent_data['props']

            # Parent's position
            tp = 2. * np.pi * float(i / (parent_props['frames'] - 1.))
            parent_x = parent_props['eccentricity'] + (parent_props['radA'] * np.cos(tp))
            parent_y = parent_props['radP'] * np.sin(tp)

            # Moon's position relative to parent
            x_marker = parent_x + (radA * np.cos(t))
            y_marker = parent_y + (radP * np.sin(t))
        else:
            # Planet or other body orbiting the Sun
            x_marker = ecc + (radA * np.cos(t))
            y_marker = radP * np.sin(t)

        # Update marker
        body_marker.set_data([x_marker], [y_marker])

        # Update trail
        xdata.append(x_marker)
        ydata.append(y_marker)
        body_line.set_data(xdata, ydata)

        return body_marker, body_line

    # Create animation
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=Nframes, interval=tinterval,
                                   blit=False)
    animations.append(anim)

    return anim

# Create animations for all bodies
bodies = data['bodies']

for body_name, body_props in bodies.items():
    print(f"Creating animation for {body_name}...")

    # Create animation for the main body
    create_body_animation(body_name, body_props)

    # Create animations for moons if they exist
    if 'moons' in body_props:
        for moon_name, moon_props in body_props['moons'].items():
            full_moon_name = f"{body_name}_{moon_name}"
            print(f"  Creating animation for {moon_name}...")
            create_body_animation(full_moon_name, moon_props, parent_name=body_name)

print(f"\nTotal animations created: {len(animations)}")
print("Displaying solar system animation...")
plt.show()
