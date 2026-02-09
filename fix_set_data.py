import re

# Read the file
with open('SolarSystem.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all set_data calls that pass two parameters directly
# Pattern: circle.set_data(x_marker, y_marker) -> circle.set_data([x_marker], [y_marker])
pattern = r'\.set_data\(([a-zA-Z_][a-zA-Z0-9_]*),\s*([a-zA-Z_][a-zA-Z0-9_]*)\)'
replacement = r'.set_data([\1], [\2])'

content = re.sub(pattern, replacement, content)

# Write the fixed content back
with open('SolarSystem.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed all set_data calls!")
