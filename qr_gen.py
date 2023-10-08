import qrcode
import svgwrite

QR_DATA = "this is a very long text"

qr = qrcode.QRCode(border=0)
qr.add_data(QR_DATA)

# Get the QR code matrix
qr_matrix = qr.get_matrix()

# Get the width of the QR code
qr_width = len(qr_matrix)

# Define the size of the region to exclude (13x13)
exclude_size = 8

# Create a Python array for the QR code matrix
qr_array = [[qr_matrix[y][x] for x in range(qr_width)] for y in range(qr_width)]

print(len(qr_array))

# Function to exclude and set pixels to 0/false for specified regions
def exclude_region(matrix, x_start, y_start, size):
    for y in range(y_start, y_start + size):
        for x in range(x_start, x_start + size):
            matrix[y][x] = False

# Exclude the top-left, top-right, and bottom-left 13x13 regions
exclude_region(qr_array, 0, 0, exclude_size)  # Top-left
exclude_region(qr_array, qr_width - exclude_size, 0, exclude_size)  # Top-right
exclude_region(qr_array, 0, qr_width - exclude_size, exclude_size)  # Bottom-left

# Define the SVG drawing with the viewBox attribute
dwg = svgwrite.Drawing('qr_export.svg', viewBox=f"-1 -1 {qr_width+2} {qr_width+2}")

# Define the cell size in millimeters, circle radius, and color for 1s (black)
cell_size_mm = 1  # 1mm
circle_radius = 0.45
cell_color = 'black'
padding = 0.1

# Create a path for the circles
path_data = ''

# Loop through the 2D array and add circle elements to the path, excluding the finder patterns
for row_idx, row in enumerate(qr_array):
    for col_idx, value in enumerate(row):
        if value:
            cx = (col_idx + 0.5) * cell_size_mm
            cy = (row_idx + 0.05) * cell_size_mm
            # Add a circle command to the path data string
            path_data += f'M{cx},{cy}a{circle_radius},{circle_radius} 0 0,0 0,{2*circle_radius}a{circle_radius},{circle_radius} 0 0,0 0,{-2*circle_radius}z'



def generate_exclude_path(x_start, y_start, size):
    path_data = []
    path_data.append(f'M{x_start + 1.75},{y_start + 0.0}h3.5a1.75,1.75 0 0 1 1.75,1.75v3.5a1.75,1.75 0 0 1 -1.75,1.75h-3.5a1.75,1.75 0 0 1 -1.75,-1.75v-3.5a1.75,1.75 0 0 1 1.75,-1.75z')
    path_data.append(f'M{x_start + 2.25},{y_start + 1.0}h2.5a1.25,1.25 0 0 1 1.25,1.25v2.5a1.25,1.25 0 0 1 -1.25,1.25h-2.5a1.25,1.25 0 0 1 -1.25,-1.25v-2.5a1.25,1.25 0 0 1 1.25,-1.25z')
    path_data.append(f'M{x_start + 2.75},{y_start + 2.0}h1.5a0.75,0.75 0 0 1 0.75,0.75v1.5a0.75,0.75 0 0 1 -0.75,0.75h-1.5a0.75,0.75 0 0 1 -0.75,-0.75v-1.5a0.75,0.75 0 0 1 0.75,-0.75z')
    return " ".join(path_data)

top_left_path = generate_exclude_path(0, 0, 13)
top_right_path = generate_exclude_path(qr_width-7, 0, 13-8)
bottom_left_path = generate_exclude_path(0, qr_width-7, 13)

# Add the paths for the excluded regions
dwg.add(dwg.path(d=top_left_path, fill=cell_color, fill_rule="evenodd"))
dwg.add(dwg.path(d=top_right_path, fill=cell_color, fill_rule="evenodd"))
dwg.add(dwg.path(d=bottom_left_path, fill=cell_color, fill_rule="evenodd"))


# Add the path data for the circles
dwg.add(dwg.path(d=path_data, fill=cell_color))

# Save the SVG file
dwg.save()
