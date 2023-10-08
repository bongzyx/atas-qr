import qrcode
import svgwrite
import cairosvg

QR_DATA = "this is a very long text"

qr = qrcode.QRCode(border=0)
qr.add_data(QR_DATA)

qr_matrix = qr.get_matrix()
qr_width = len(qr_matrix)

exclude_size = 8

qr_array = [[qr_matrix[y][x] for x in range(qr_width)] for y in range(qr_width)]

def exclude_region(matrix, x_start, y_start, size):
    for y in range(y_start, y_start + size):
        for x in range(x_start, x_start + size):
            matrix[y][x] = False

exclude_region(qr_array, 0, 0, exclude_size)  # top-left
exclude_region(qr_array, qr_width - exclude_size, 0, exclude_size)  # top-right
exclude_region(qr_array, 0, qr_width - exclude_size, exclude_size)  # bottom-left

dwg = svgwrite.Drawing('qr_export.svg', viewBox=f"-1 -1 {qr_width+2} {qr_width+2}")

cell_size_mm = 1
circle_radius = 0.45
cell_color = 'black'
padding = 0.1

dots_data_path = ''

for row_idx, row in enumerate(qr_array):
    for col_idx, value in enumerate(row):
        if value:
            cx = (col_idx + 0.5) * cell_size_mm
            cy = (row_idx + 0.05) * cell_size_mm
            dots_data_path += f'M{cx},{cy}a{circle_radius},{circle_radius} 0 0,0 0,{2*circle_radius}a{circle_radius},{circle_radius} 0 0,0 0,{-2*circle_radius}z'

def generate_finder_eye_path(x_start, y_start):
    finder_eye_path = []
    finder_eye_path.append(f'M{x_start + 1.75},{y_start + 0.0}h3.5a1.75,1.75 0 0 1 1.75,1.75v3.5a1.75,1.75 0 0 1 -1.75,1.75h-3.5a1.75,1.75 0 0 1 -1.75,-1.75v-3.5a1.75,1.75 0 0 1 1.75,-1.75z')
    finder_eye_path.append(f'M{x_start + 2.25},{y_start + 1.0}h2.5a1.25,1.25 0 0 1 1.25,1.25v2.5a1.25,1.25 0 0 1 -1.25,1.25h-2.5a1.25,1.25 0 0 1 -1.25,-1.25v-2.5a1.25,1.25 0 0 1 1.25,-1.25z')
    finder_eye_path.append(f'M{x_start + 2.75},{y_start + 2.0}h1.5a0.75,0.75 0 0 1 0.75,0.75v1.5a0.75,0.75 0 0 1 -0.75,0.75h-1.5a0.75,0.75 0 0 1 -0.75,-0.75v-1.5a0.75,0.75 0 0 1 0.75,-0.75z')
    return " ".join(finder_eye_path)

top_left_path = generate_finder_eye_path(0, 0)
top_right_path = generate_finder_eye_path(qr_width-7, 0)
bottom_left_path = generate_finder_eye_path(0, qr_width-7)

dwg.add(dwg.path(d=top_left_path, fill=cell_color, fill_rule="evenodd"))
dwg.add(dwg.path(d=top_right_path, fill=cell_color, fill_rule="evenodd"))
dwg.add(dwg.path(d=bottom_left_path, fill=cell_color, fill_rule="evenodd"))

dwg.add(dwg.path(d=dots_data_path, fill=cell_color))

dwg.save()

png_size = 1024
cairosvg.svg2png(url='qr_export.svg', write_to='qr_export.png', output_height=png_size, output_width=png_size)