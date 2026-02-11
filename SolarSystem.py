import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Load celestial bodies data from JSON
with open('celestial_bodies.json', 'r') as f:
    data = json.load(f)

# Extract simulation parameters
sim = data['simulation']
Nframes = sim['Nframes']
rad = sim['rad']
tinterval = sim['tinterval']

# Store all trajectory data
trajectories = {}
bodies_list = []
primary_bodies = []  # Non-moon bodies for sidebar


def calculate_3d_position(t, radP, radA, rad, ecc, inclination, parent_pos=None):
    """Calculate 3D position with orbital inclination"""
    inc_rad = np.radians(inclination)

    # Calculate ellipse parameters
    # Semi-major axis (average distance)
    a = rad
    # Semi-minor axis (calculated from periapsis and apoapsis)
    b = np.sqrt(radP * radA)
    # Linear eccentricity (distance from center to focus where parent is)
    c = a * ecc

    # Basic elliptical orbit in the xy-plane
    # Ellipse centered at origin, then shifted so parent is at focus
    x = a * np.cos(t) - c
    y = b * np.sin(t)

    # Apply inclination (rotate around x-axis)
    y_inclined = y * np.cos(inc_rad)
    z_inclined = y * np.sin(inc_rad)

    # If orbiting a parent body, add parent's position
    if parent_pos is not None:
        x += parent_pos[0]
        y_inclined += parent_pos[1]
        z_inclined += parent_pos[2]

    return x, y_inclined, z_inclined


def generate_trajectories(name, body_props, parent_name=None):
    """Generate complete orbital trajectory for a body"""
    radP = body_props['radP']
    radA = body_props['radA']
    rad = body_props['rad']  # Semi-major axis
    orbital_period_days = body_props['frames']  # Orbital period in Earth days
    ecc = body_props['eccentricity']
    inclination = body_props.get('inclination', 0.0)
    color = body_props['color']
    marker_size = body_props['markerSize']
    body_type = body_props.get('type', 'unknown')

    # Generate time points for full orbit
    x_traj = []
    y_traj = []
    z_traj = []

    # Total simulation time in days (12 years)
    total_sim_days = 4380.0
    days_per_frame = total_sim_days / Nframes

    for i in range(Nframes):
        # Get parent position if it's a moon
        parent_pos = None
        if parent_name and parent_name in trajectories:
            parent_data = trajectories[parent_name]
            if i < len(parent_data['x']):
                parent_pos = (
                    parent_data['x'][i],
                    parent_data['y'][i],
                    parent_data['z'][i]
                )

        # Calculate position for this body
        # days_elapsed = current simulation frame * days per frame
        # angle = 2π * (days_elapsed / orbital_period)
        days_elapsed = i * days_per_frame
        t_body = 2. * np.pi * (days_elapsed / orbital_period_days) if orbital_period_days > 0 else 0
        x, y, z = calculate_3d_position(t_body, radP, radA, rad, ecc, inclination, parent_pos)

        x_traj.append(x)
        y_traj.append(y)
        z_traj.append(z)

    # Store trajectory data
    trajectories[name] = {
        'x': np.array(x_traj),
        'y': np.array(y_traj),
        'z': np.array(z_traj),
        'color': color,
        'marker_size': marker_size,
        'body_type': body_type,
        'name': name.split('_')[-1] if '_' in name else name,
        'parent': parent_name,
        'is_primary': parent_name is None  # Primary bodies don't orbit other bodies
    }

    bodies_list.append(name)
    if parent_name is None:  # This is a primary body
        primary_bodies.append(name)


# Generate trajectories for all bodies
print("Generating 3D trajectories for 12 years of simulation at 30 FPS...")
print("This may take a minute with 41 bodies and 131,400 frames...")
print("Pre-calculating smooth orbital motion - please wait...")
bodies = data['bodies']

body_count = 0
total_estimated = 41

for body_name, body_props in bodies.items():
    body_count += 1
    print(f"  [{body_count}/{total_estimated}] {body_name}...")
    generate_trajectories(body_name, body_props)

    # Generate trajectories for moons
    if 'moons' in body_props:
        for moon_name, moon_props in body_props['moons'].items():
            body_count += 1
            full_moon_name = f"{body_name}_{moon_name}"
            print(f"    [{body_count}/{total_estimated}] {moon_name}...")
            generate_trajectories(full_moon_name, moon_props, parent_name=body_name)

print(f"\nTotal bodies generated: {len(bodies_list)}")
print(f"Primary bodies: {len(primary_bodies)}")
print("Building matplotlib 3D figure with GPU acceleration...")

# Create figure and 3D axis (leave space for sidebar on right)
fig = plt.figure(figsize=(18, 12))
fig.patch.set_facecolor('#001219')
ax = fig.add_subplot(111, projection='3d', facecolor='#001219', position=[0.05, 0.1, 0.68, 0.85])

# Set axis limits and styling
ax.set_xlim(-rad, rad)
ax.set_ylim(-rad, rad)
ax.set_zlim(-rad/2, rad/2)
ax.set_xlabel('X (AU)', color='white', fontsize=12)
ax.set_ylabel('Y (AU)', color='white', fontsize=12)
ax.set_zlabel('Z (AU)', color='white', fontsize=12)
ax.set_title('3D Solar System - Real Orbital Inclinations', color='white', fontsize=16, pad=20)

# Style the grid and background
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('#1a3a4a')
ax.yaxis.pane.set_edgecolor('#1a3a4a')
ax.zaxis.pane.set_edgecolor('#1a3a4a')
ax.grid(True, alpha=0.2, color='#4a6a7a')
ax.tick_params(colors='white')

# Set initial viewing angle
ax.view_init(elev=20, azim=45)

# Store plot objects
orbit_lines = {}
body_markers = {}
body_labels = {}

# Create orbit lines and markers for each body
for body_name in bodies_list:
    traj = trajectories[body_name]
    is_major = traj['body_type'] in ['planet', 'star', 'dwarf_planet']

    # Orbit trail (line)
    line, = ax.plot([], [], [],
                    color=traj['color'],
                    linewidth=1.5 if is_major else 0.8,
                    alpha=0.4,
                    label=traj['name'])
    orbit_lines[body_name] = line

    # Body marker
    marker, = ax.plot([], [], [],
                      marker='o',
                      markersize=traj['marker_size'] * 2,
                      color=traj['color'],
                      markeredgecolor='white',
                      markeredgewidth=0.5)
    body_markers[body_name] = marker

    # Label
    label = ax.text(0, 0, 0, traj['name'],
                   color='white',
                   fontsize=10 if is_major else 7,
                   fontweight='bold' if is_major else 'normal')
    body_labels[body_name] = label

# Animation state
current_frame = [0]
is_paused = [False]
speed_multiplier = [1.0]
show_labels = [True]
show_orbits = [True]
focused_body = ['Sun']  # Default focus on Sun
camera_distance = [50]  # Distance from focused body
camera_elevation = [20]
camera_azimuth = [45]
free_cam_mode = [False]

# Animation function
def animate(frame):
    if is_paused[0]:
        return []

    current_frame[0] = (current_frame[0] + int(speed_multiplier[0])) % Nframes
    idx = current_frame[0]

    artists = []

    for body_name in bodies_list:
        traj = trajectories[body_name]

        # Update orbit trail (show up to current position)
        if show_orbits[0]:
            orbit_lines[body_name].set_data(traj['x'][:idx+1], traj['y'][:idx+1])
            orbit_lines[body_name].set_3d_properties(traj['z'][:idx+1])
        else:
            orbit_lines[body_name].set_data([], [])
            orbit_lines[body_name].set_3d_properties([])
        artists.append(orbit_lines[body_name])

        # Update body marker position
        body_markers[body_name].set_data([traj['x'][idx]], [traj['y'][idx]])
        body_markers[body_name].set_3d_properties([traj['z'][idx]])
        artists.append(body_markers[body_name])

        # Update label position
        if show_labels[0]:
            body_labels[body_name].set_position((traj['x'][idx], traj['y'][idx]))
            body_labels[body_name].set_3d_properties(traj['z'][idx], 'z')
            body_labels[body_name].set_visible(True)
        else:
            body_labels[body_name].set_visible(False)
        artists.append(body_labels[body_name])

    # Update camera to follow focused body (if not in free cam mode)
    if not free_cam_mode[0] and focused_body[0] in trajectories:
        focus_traj = trajectories[focused_body[0]]
        focus_x = focus_traj['x'][idx]
        focus_y = focus_traj['y'][idx]
        focus_z = focus_traj['z'][idx]

        # Calculate camera position based on elevation and azimuth
        elev_rad = np.radians(camera_elevation[0])
        azim_rad = np.radians(camera_azimuth[0])

        # Camera offset from focused body
        cam_dist = camera_distance[0]
        cam_x = focus_x + cam_dist * np.cos(elev_rad) * np.cos(azim_rad)
        cam_y = focus_y + cam_dist * np.cos(elev_rad) * np.sin(azim_rad)
        cam_z = focus_z + cam_dist * np.sin(elev_rad)

        # Set view to look at focused body
        ax.set_xlim(focus_x - cam_dist/2, focus_x + cam_dist/2)
        ax.set_ylim(focus_y - cam_dist/2, focus_y + cam_dist/2)
        ax.set_zlim(focus_z - cam_dist/4, focus_z + cam_dist/4)

    # Update compass gizmo to match current view (read actual view angles from ax)
    current_elev = ax.elev
    current_azim = ax.azim
    if current_elev != camera_elevation[0] or current_azim != camera_azimuth[0]:
        camera_elevation[0] = current_elev
        camera_azimuth[0] = current_azim

    return artists

# Create animation
print("Creating animation...")
anim = animation.FuncAnimation(fig, animate, frames=Nframes,
                              interval=tinterval/speed_multiplier[0],
                              blit=False, cache_frame_data=False)  # blit=False allows axis updates for tracking

# Control panel
ax_pause = plt.axes([0.08, 0.02, 0.08, 0.04])
ax_reset = plt.axes([0.17, 0.02, 0.08, 0.04])
ax_speed = plt.axes([0.30, 0.02, 0.25, 0.03])
ax_labels = plt.axes([0.57, 0.02, 0.08, 0.04])
ax_freecam = plt.axes([0.66, 0.02, 0.08, 0.04])

btn_pause = Button(ax_pause, 'Pause', color='#1a3a4a', hovercolor='#2a5a6a')
btn_reset = Button(ax_reset, 'Reset', color='#1a3a4a', hovercolor='#2a5a6a')
slider_speed = Slider(ax_speed, 'Speed', 1, 100, valinit=1, valstep=1, color='#4a8a9a')
btn_labels = Button(ax_labels, 'Labels: ON', color='#1a3a4a', hovercolor='#2a5a6a')
btn_freecam = Button(ax_freecam, 'Free Cam', color='#3a1a4a', hovercolor='#5a2a6a')

def pause_animation(event):
    is_paused[0] = not is_paused[0]
    btn_pause.label.set_text('Play' if is_paused[0] else 'Pause')

def reset_view(event):
    ax.view_init(elev=20, azim=45)
    camera_elevation[0] = 20
    camera_azimuth[0] = 45
    ax.set_xlim(-rad, rad)
    ax.set_ylim(-rad, rad)
    ax.set_zlim(-rad/2, rad/2)
    update_compass_gizmo()
    plt.draw()

def update_speed(val):
    speed_multiplier[0] = val
    anim.event_source.interval = tinterval / speed_multiplier[0]

def toggle_labels(event):
    show_labels[0] = not show_labels[0]
    btn_labels.label.set_text(f'Labels: {"ON" if show_labels[0] else "OFF"}')

def toggle_freecam(event):
    free_cam_mode[0] = not free_cam_mode[0]
    if free_cam_mode[0]:
        btn_freecam.label.set_text('Locked')
        btn_freecam.color = '#1a4a3a'
        # Reset to full view when entering free cam
        ax.set_xlim(-rad, rad)
        ax.set_ylim(-rad, rad)
        ax.set_zlim(-rad/2, rad/2)
    else:
        btn_freecam.label.set_text('Free Cam')
        btn_freecam.color = '#3a1a4a'
    plt.draw()

def focus_on_body(body_name):
    """Focus camera on a specific body"""
    def handler(event):
        focused_body[0] = body_name
        free_cam_mode[0] = False
        btn_freecam.label.set_text('Free Cam')
        btn_freecam.color = '#3a1a4a'

        # Set camera distance: 0.2 AU for all bodies except Sun
        if body_name == 'Sun':
            camera_distance[0] = 50  # Full solar system view
        else:
            camera_distance[0] = 0.4  # 0.2 AU radius (0.4 total width)

        # Highlight selected button
        for btn in focus_buttons.values():
            btn.color = '#1a3a4a'
        if body_name in focus_buttons:
            focus_buttons[body_name].color = '#4a6a1a'

        plt.draw()
    return handler

btn_pause.on_clicked(pause_animation)
btn_reset.on_clicked(reset_view)
slider_speed.on_changed(update_speed)
btn_labels.on_clicked(toggle_labels)
btn_freecam.on_clicked(toggle_freecam)

# Create sidebar with focus buttons for primary bodies
print("Creating focus sidebar...")
sidebar_x = 0.76
sidebar_width = 0.13
button_height = 0.035
button_spacing = 0.04

# Add sidebar title
fig.text(sidebar_x + sidebar_width/2, 0.95, 'FOCUS ON:',
         ha='center', va='top', color='white', fontsize=12, weight='bold')

focus_buttons = {}
y_pos = 0.92

for i, body_name in enumerate(primary_bodies):
    traj = trajectories[body_name]
    ax_btn = plt.axes([sidebar_x, y_pos - i * button_spacing, sidebar_width, button_height])

    # Color code button by body color
    btn_color = '#4a6a1a' if body_name == 'Sun' else '#1a3a4a'
    btn = Button(ax_btn, traj['name'], color=btn_color, hovercolor='#2a5a6a')
    btn.label.set_color(traj['color'])
    btn.label.set_fontsize(9)
    btn.on_clicked(focus_on_body(body_name))
    focus_buttons[body_name] = btn

# Create 3D View Compass Gizmo (visual graphic) in bottom right
print("Creating 3D view compass gizmo...")
from matplotlib.patches import Circle

# Create a separate axes for the compass gizmo
compass_ax = plt.axes([0.78, 0.08, 0.10, 0.10], facecolor='#0a0a0a')
compass_ax.set_xlim(-1.5, 1.5)
compass_ax.set_ylim(-1.5, 1.5)
compass_ax.set_aspect('equal')
compass_ax.axis('off')

# Add title above gizmo
fig.text(0.83, 0.19, 'VIEW', ha='center', va='bottom',
         color='white', fontsize=9, weight='bold')

# Define 3D world positions for each axis direction
axis_vectors_3d = {
    '+X': np.array([1.2, 0.0, 0.0]),
    '-X': np.array([-1.2, 0.0, 0.0]),
    '+Y': np.array([0.0, 1.2, 0.0]),
    '-Y': np.array([0.0, -1.2, 0.0]),
    '+Z': np.array([0.0, 0.0, 1.2]),
    '-Z': np.array([0.0, 0.0, -1.2]),
}

axis_colors = {
    '+X': '#ff4444',  # Bright red
    '-X': '#884444',  # Dark red
    '+Y': '#44ff44',  # Bright green
    '-Y': '#448844',  # Dark green
    '+Z': '#4444ff',  # Bright blue
    '-Z': '#444488',  # Dark blue
}

axis_views = {
    '+X': (0, 0),      # Front
    '-X': (0, 180),    # Back
    '+Y': (0, 90),     # Right
    '-Y': (0, -90),    # Left
    '+Z': (90, 0),     # Top
    '-Z': (-90, 0),    # Bottom
}

# Create compass elements (will be updated dynamically)
compass_lines = {}
compass_circles = {}
compass_labels = {}

# Draw center dot
center_circle = Circle((0, 0), 0.15, facecolor='#666666',
                      edgecolor='#888888', linewidth=1,
                      picker=True, zorder=10)
compass_ax.add_patch(center_circle)

# Create lines and circles for each axis
for axis_name in axis_vectors_3d.keys():
    # Line from center to axis endpoint
    line, = compass_ax.plot([], [], color=axis_colors[axis_name],
                           linewidth=2, alpha=0.6, zorder=5)
    compass_lines[axis_name] = line

    # Circle at axis endpoint (clickable)
    circle = Circle((0, 0), 0.25, facecolor=axis_colors[axis_name],
                   edgecolor=axis_colors[axis_name], linewidth=2,
                   picker=True, zorder=20)
    compass_ax.add_patch(circle)
    compass_circles[axis_name] = circle

    # Label
    label = compass_ax.text(0, 0, axis_name.replace('+', '').replace('-', ''),
                          ha='center', va='center',
                          color='white', fontsize=7, weight='bold',
                          zorder=30)
    compass_labels[axis_name] = label

def project_axis_to_compass(axis_3d, elev, azim):
    """Project a 3D axis vector to 2D compass position based on view angle"""
    # Convert angles to radians
    elev_rad = np.radians(elev)
    azim_rad = np.radians(azim)

    # Rotation matrices for view transformation
    # Azimuth rotation (around Z)
    cos_az, sin_az = np.cos(azim_rad), np.sin(azim_rad)
    rot_z = np.array([
        [cos_az, -sin_az, 0],
        [sin_az, cos_az, 0],
        [0, 0, 1]
    ])

    # Elevation rotation (around rotated X)
    cos_el, sin_el = np.cos(elev_rad), np.sin(elev_rad)
    rot_x = np.array([
        [1, 0, 0],
        [0, cos_el, -sin_el],
        [0, sin_el, cos_el]
    ])

    # Apply rotations
    rotated = rot_z @ rot_x @ axis_3d

    # Project to 2D (use x and z, since we're looking along y)
    return rotated[0], rotated[2]

def update_compass_gizmo():
    """Update compass gizmo to match current view orientation"""
    elev = camera_elevation[0]
    azim = camera_azimuth[0]

    for axis_name, axis_vec in axis_vectors_3d.items():
        # Project 3D axis to 2D compass position
        x_2d, y_2d = project_axis_to_compass(axis_vec, elev, azim)

        # Update line
        compass_lines[axis_name].set_data([0, x_2d], [0, y_2d])

        # Update circle position
        compass_circles[axis_name].center = (x_2d, y_2d)

        # Update label position (slightly offset from circle)
        label_offset = 0.35
        label_x = x_2d + (label_offset if x_2d > 0 else -label_offset if x_2d < 0 else 0)
        label_y = y_2d + (label_offset if y_2d > 0 else -label_offset if y_2d < 0 else 0)
        compass_labels[axis_name].set_position((label_x, label_y))

        # Adjust visibility and alpha based on depth (z component after rotation)
        elev_rad = np.radians(elev)
        azim_rad = np.radians(azim)
        cos_az, sin_az = np.cos(azim_rad), np.sin(azim_rad)
        cos_el, sin_el = np.cos(elev_rad), np.sin(elev_rad)
        rot_z = np.array([[cos_az, -sin_az, 0], [sin_az, cos_az, 0], [0, 0, 1]])
        rot_x = np.array([[1, 0, 0], [0, cos_el, -sin_el], [0, sin_el, cos_el]])
        rotated = rot_z @ rot_x @ axis_vec

        # Depth is the y-component (into screen)
        depth = rotated[1]
        if depth > 0:  # Facing away
            compass_circles[axis_name].set_alpha(0.3)
            compass_labels[axis_name].set_alpha(0.3)
        else:  # Facing toward viewer
            compass_circles[axis_name].set_alpha(1.0)
            compass_labels[axis_name].set_alpha(1.0)

# Initialize compass with current view
update_compass_gizmo()

# Mouse click handler for compass
def on_compass_click(event):
    """Handle clicks on compass gizmo"""
    if event.inaxes == compass_ax:
        for axis_name, circle in compass_circles.items():
            if circle.contains(event)[0]:
                elev, azim = axis_views[axis_name]
                camera_elevation[0] = elev
                camera_azimuth[0] = azim
                ax.view_init(elev=elev, azim=azim)
                update_compass_gizmo()

                # Highlight clicked circle
                for name, circ in compass_circles.items():
                    if name == axis_name:
                        circ.set_edgecolor('white')
                        circ.set_linewidth(3)
                    else:
                        circ.set_edgecolor(axis_colors[name])
                        circ.set_linewidth(2)

                plt.draw()
                break

fig.canvas.mpl_connect('button_press_event', on_compass_click)

# Keyboard shortcuts
def on_key(event):
    if event.key == ' ':  # Spacebar
        pause_animation(None)
    elif event.key == 'r':  # Reset
        reset_view(None)
    elif event.key == 'l':  # Toggle labels
        toggle_labels(None)
    elif event.key == 'o':  # Toggle orbits
        show_orbits[0] = not show_orbits[0]
    elif event.key == 'f':  # Toggle free cam
        toggle_freecam(None)
    elif event.key == '+' or event.key == '=':  # Speed up
        new_speed = min(100, speed_multiplier[0] + 5)
        slider_speed.set_val(new_speed)
    elif event.key == '-' or event.key == '_':  # Slow down
        new_speed = max(1, speed_multiplier[0] - 5)
        slider_speed.set_val(new_speed)
    elif event.key == 'up':  # Zoom in
        camera_distance[0] = max(0.00001, camera_distance[0] * 0.8)  # Super close zoom for inner moons!
    elif event.key == 'down':  # Zoom out
        camera_distance[0] = min(200, camera_distance[0] * 1.2)
    elif event.key == 'left':  # Rotate left
        camera_azimuth[0] = (camera_azimuth[0] - 10) % 360
        ax.view_init(elev=camera_elevation[0], azim=camera_azimuth[0])
        update_compass_gizmo()
    elif event.key == 'right':  # Rotate right
        camera_azimuth[0] = (camera_azimuth[0] + 10) % 360
        ax.view_init(elev=camera_elevation[0], azim=camera_azimuth[0])
        update_compass_gizmo()

fig.canvas.mpl_connect('key_press_event', on_key)

# Update compass when view is rotated with mouse
def on_mouse_move(event):
    """Update compass when user drags to rotate view"""
    if event.inaxes == ax and event.button is not None:
        # User is dragging the view - update compass
        current_elev = ax.elev
        current_azim = ax.azim
        if abs(current_elev - camera_elevation[0]) > 0.5 or abs(current_azim - camera_azimuth[0]) > 0.5:
            camera_elevation[0] = current_elev
            camera_azimuth[0] = current_azim
            update_compass_gizmo()
            fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

# Mouse wheel zoom
def on_scroll(event):
    """Handle mouse wheel for zooming"""
    if event.button == 'up':  # Scroll up = zoom in
        camera_distance[0] = max(0.00001, camera_distance[0] * 0.9)  # Super close zoom for inner moons!
    elif event.button == 'down':  # Scroll down = zoom out
        camera_distance[0] = min(200, camera_distance[0] * 1.1)
    plt.draw()

fig.canvas.mpl_connect('scroll_event', on_scroll)

# Print controls
print("\n" + "="*70)
print("3D SOLAR SYSTEM - GPU ACCELERATED WITH FOCUS MODE!")
print("="*70)
print("SIDEBAR:")
print("  - Click any body      - Focus camera on that body and follow it")
print("  - Free Cam button     - Unlock camera for manual control")
print("\nVIEW COMPASS (Bottom Right):")
print("  - +X, -X, +Y, -Y      - Jump to side orthogonal views")
print("  - +Z, -Z              - Jump to top/bottom views")
print("  Works with lock-on: view jumps while tracking focused body!")
print("\nMOUSE CONTROLS:")
print("  - Click + Drag        - Rotate view (around focused body)")
print("  - Scroll Wheel        - Zoom in/out")
print("  - Middle + Drag       - Pan")
print("\nKEYBOARD SHORTCUTS:")
print("  - SPACE               - Pause/Play")
print("  - R                   - Reset view")
print("  - L                   - Toggle labels")
print("  - O                   - Toggle orbit trails")
print("  - F                   - Toggle Free Cam mode")
print("  - +/-                 - Speed up/down")
print("  - Arrow Up/Down       - Zoom in/out from focused body")
print("  - Arrow Left/Right    - Rotate around focused body")
print("\nBUTTONS:")
print("  - Pause/Play          - Toggle animation")
print("  - Reset               - Reset camera view")
print("  - Speed slider        - 1x to 100x speed")
print("  - Labels ON/OFF       - Toggle body labels")
print("  - Free Cam            - Unlock camera from focused body")
print("="*70)
print("\nFEATURES:")
print("  - 41 celestial bodies with NASA JPL data")
print("  - 12 years of simulation (131,400 frames)")
print("  - BUTTERY SMOOTH 30 FPS animation!")
print("  - Real 3D orbital inclinations")
print("  - GPU-accelerated OpenGL rendering")
print("  - Focus & Follow mode for each primary body!")
print("  - Himalia: 28.4deg tilt!")
print("  - Triton: 157.3deg retrograde!")
print("  - Nereid: 0.751 eccentricity!")
print("="*70)
print("\nOpening 3D window...")
print("Try clicking 'Earth' in the sidebar to follow it!")
print("="*70)

# Add legend (smaller to fit with sidebar)
ax.legend(loc='upper left', fontsize=6, framealpha=0.2,
         facecolor='#001219', edgecolor='white', labelcolor='white',
         ncol=2)

# Show the plot
plt.show()

print("\nVisualization closed.")
