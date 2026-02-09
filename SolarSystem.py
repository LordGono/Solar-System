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

# Create figure with better layout
fig = plt.figure(figsize=(12, 10))
ax = plt.subplot2grid((1, 1), (0, 0),
                       xlim=(-2.*rad, 2.*rad), ylim=(-2.*rad, 2.*rad), aspect='equal')
ax.set_adjustable('box')
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_facecolor('#000814')
fig.patch.set_facecolor('#001219')

# Store animation objects and data
animations = []
bodies_data = {}
labels = {}
show_labels = True
check_overlap = True  # Toggle for overlap detection

# Zoom and pan state
zoom_scale = 1.0
pan_offset = [0, 0]
press_event = None


def check_label_overlap(name1, name2, min_distance=15):
    """Check if two labels would overlap"""
    if name1 not in bodies_data or name2 not in bodies_data:
        return False

    pos1 = bodies_data[name1]['current_pos']
    pos2 = bodies_data[name2]['current_pos']

    # Calculate distance in data coordinates
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    distance = np.sqrt(dx**2 + dy**2)

    # Check if labels might overlap (approximate)
    # Convert data distance to a rough estimate
    xlim = ax.get_xlim()
    view_width = xlim[1] - xlim[0]

    # Rough conversion: min_distance pixels in a 100-unit view
    pixel_threshold = view_width * 0.02

    return distance < pixel_threshold


def adjust_label_position(name, body_props, x_marker, y_marker):
    """Adjust label offset to avoid overlaps"""
    if not check_overlap:
        return

    # Get label type
    is_moon = bodies_data[name]['parent'] is not None

    # Only adjust moon labels to avoid planet labels
    if is_moon:
        # Check against all major bodies
        for other_name, other_data in bodies_data.items():
            if other_data['parent'] is None:  # Major body
                if check_label_overlap(name, other_name):
                    # Adjust offset to opposite side
                    label = labels[name]
                    label.xytext = (-6, -6)  # Move to bottom-left instead
                    return

    # Default offset already set in creation


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
    body_type = body_props.get('type', 'unknown')

    # Determine if this is a major body (planet, dwarf planet) or moon
    is_moon = parent_name is not None
    is_major_body = body_type in ['planet', 'star', 'dwarf_planet']

    # Create orbit circle (cosmetic)
    orbit_radius = body_props['rad']
    if orbit_radius > 0:
        orbit_circle = plt.Circle((0, 0), radius=orbit_radius,
                                  facecolor="None", edgecolor="gray",
                                  lw=0.5, alpha=0.3)
        ax.add_patch(orbit_circle)

    # Create plot elements
    body_marker, = ax.plot([], [], marker='o', ms=marker_size, color=color)
    body_line, = ax.plot([], [], lw=1, color=line_color, alpha=0.6)

    # Create label for the body
    display_name = name.split('_')[-1] if '_' in name else name

    # Configure label style based on body type
    if is_major_body:
        # Major bodies: larger, bold, higher z-order
        font_size = 9
        font_weight = 'bold'
        box_alpha = 0.75
        edge_width = 0.8
        arrow_width = 0.7
        label_zorder = 100  # Render on top
        text_offset = (10, 10)
    elif is_moon:
        # Moons: smaller, lighter, lower z-order
        font_size = 6
        font_weight = 'normal'
        box_alpha = 0.5
        edge_width = 0.3
        arrow_width = 0.4
        label_zorder = 50  # Render below planets
        text_offset = (6, 6)
    else:
        # Other bodies (asteroids, comets)
        font_size = 7
        font_weight = 'normal'
        box_alpha = 0.6
        edge_width = 0.5
        arrow_width = 0.5
        label_zorder = 75
        text_offset = (8, 8)

    # Use annotate for better label positioning with arrows
    label = ax.annotate(display_name, xy=(0, 0), xytext=text_offset,
                       textcoords='offset points',
                       fontsize=font_size, color='white',
                       weight=font_weight,
                       ha='left', va='bottom', alpha=0.9,
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='black',
                                alpha=box_alpha, edgecolor='gray', linewidth=edge_width),
                       arrowprops=dict(arrowstyle='-', color='gray',
                                      alpha=0.4, lw=arrow_width),
                       zorder=label_zorder)
    labels[name] = label

    # Data storage
    xdata = []
    ydata = []

    # Store in global dict
    bodies_data[name] = {
        'marker': body_marker,
        'line': body_line,
        'label': label,
        'xdata': xdata,
        'ydata': ydata,
        'props': body_props,
        'parent': parent_name,
        'current_pos': (0, 0)
    }

    # Init function
    def init():
        body_marker.set_data([], [])
        body_line.set_data([], [])
        label.xy = (0, 0)
        label.set_visible(show_labels)
        return body_marker, body_line, label

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

        # Store current position
        bodies_data[name]['current_pos'] = (x_marker, y_marker)

        # Update marker
        body_marker.set_data([x_marker], [y_marker])

        # Update trail
        xdata.append(x_marker)
        ydata.append(y_marker)
        body_line.set_data(xdata, ydata)

        # Update label position (annotation follows the body)
        label.xy = (x_marker, y_marker)
        label.set_visible(show_labels)

        # Check for overlaps and adjust if needed
        adjust_label_position(name, body_props, x_marker, y_marker)

        return body_marker, body_line, label

    # Create animation
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=Nframes, interval=tinterval,
                                   blit=False)
    animations.append(anim)

    return anim


def on_scroll(event):
    """Handle mouse wheel zoom"""
    global zoom_scale

    if event.inaxes != ax:
        return

    # Get current axis limits
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Get mouse position
    xdata = event.xdata
    ydata = event.ydata

    # Zoom factor
    if event.button == 'up':
        scale_factor = 0.9  # Zoom in
    elif event.button == 'down':
        scale_factor = 1.1  # Zoom out
    else:
        return

    # Calculate new limits centered on mouse position
    x_center = xdata
    y_center = ydata

    x_width = (xlim[1] - xlim[0]) * scale_factor
    y_height = (ylim[1] - ylim[0]) * scale_factor

    new_xlim = [x_center - x_width/2, x_center + x_width/2]
    new_ylim = [y_center - y_height/2, y_center + y_height/2]

    ax.set_xlim(new_xlim)
    ax.set_ylim(new_ylim)

    fig.canvas.draw_idle()


def on_press(event):
    """Handle mouse press for panning"""
    global press_event
    if event.inaxes != ax:
        return
    press_event = event


def on_release(event):
    """Handle mouse release"""
    global press_event
    press_event = None


def on_motion(event):
    """Handle mouse motion for panning"""
    global press_event

    if press_event is None or event.inaxes != ax:
        return

    # Calculate drag distance
    dx = event.xdata - press_event.xdata
    dy = event.ydata - press_event.ydata

    # Update axis limits
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    ax.set_xlim([xlim[0] - dx, xlim[1] - dx])
    ax.set_ylim([ylim[0] - dy, ylim[1] - dy])

    fig.canvas.draw_idle()


def on_key(event):
    """Handle keyboard shortcuts"""
    global show_labels, check_overlap

    if event.key == 'l':
        # Toggle labels
        show_labels = not show_labels
        for label in labels.values():
            label.set_visible(show_labels)
        fig.canvas.draw_idle()

    elif event.key == 'r':
        # Reset view
        ax.set_xlim(-2.*rad, 2.*rad)
        ax.set_ylim(-2.*rad, 2.*rad)
        fig.canvas.draw_idle()

    elif event.key == 'g':
        # Toggle grid
        ax.grid(not ax.xaxis._gridOnMajor)
        fig.canvas.draw_idle()

    elif event.key == 'o':
        # Toggle overlap detection
        check_overlap = not check_overlap
        status = "ON" if check_overlap else "OFF"
        print(f"Label overlap detection: {status}")
        fig.canvas.draw_idle()


# Connect event handlers
fig.canvas.mpl_connect('scroll_event', on_scroll)
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('key_press_event', on_key)

# Add control instructions
controls_text = (
    "Controls:\n"
    "• Mouse Wheel: Zoom in/out\n"
    "• Click + Drag: Pan view\n"
    "• L: Toggle labels\n"
    "• G: Toggle grid\n"
    "• O: Overlap detection\n"
    "• R: Reset view"
)
ax.text(0.02, 0.98, controls_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='black', alpha=0.7),
        color='white', family='monospace')

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
print("\n" + "="*50)
print("INTERACTIVE CONTROLS")
print("="*50)
print("• Mouse Wheel     - Zoom in/out")
print("• Click + Drag    - Pan view")
print("• L key          - Toggle labels")
print("• G key          - Toggle grid")
print("• O key          - Overlap detection")
print("• R key          - Reset view")
print("="*50)
print("\nLabel Hierarchy:")
print("  * Planets/Stars  - Large, bold labels (always on top)")
print("  - Moons         - Small labels (render below)")
print("  + Other bodies  - Medium labels")
print("="*50)
print("\nDisplaying solar system animation...")

plt.tight_layout()
plt.show()
