from turtle import width
from cairosvg import svg2png
import qrcode
import svgwrite


def gen_qr(data="some text here"):
    POSITION_DETECTION_RADIUS = 6.5
    POSITION_DETECTION_COLOUR = "#191715"
    BORDER_COLOUR = "#191715"
    BORDER_BACKGROUND_COLOUR = "white"
    BORDER_RADIUS = 12

    QR_DATA = data

    version_list = [{'version': 1, 'width': 21, 'maxChar': 25},
                    {'version': 2, 'width': 25, 'maxChar': 47},
                    {'version': 3, 'width': 29, 'maxChar': 77},
                    {'version': 4, 'width': 3, 'maxChar': 114},
                    {'version': 5, 'width': 37, 'maxChar': 154},
                    {'version': 6, 'width': 41, 'maxChar': 195},
                    {'version': 7, 'width': 45, 'maxChar': 224},
                    {'version': 8, 'width': 49, 'maxChar': 279},
                    {'version': 9, 'width': 53, 'maxChar': 335},
                    {'version': 10, 'width': 57, 'maxChar': 395},
                    {'version': 11, 'width': 61, 'maxChar': 468},
                    {'version': 12, 'width': 65, 'maxChar': 535},
                    {'version': 13, 'width': 69, 'maxChar': 619},
                    {'version': 14, 'width': 73, 'maxChar': 667},
                    {'version': 15, 'width': 77, 'maxChar': 758},
                    {'version': 16, 'width': 81, 'maxChar': 854},
                    {'version': 17, 'width': 85, 'maxChar': 938},
                    {'version': 18, 'width': 89, 'maxChar': 1046},
                    {'version': 19, 'width': 93, 'maxChar': 1153},
                    {'version': 20, 'width': 97, 'maxChar': 1249},
                    {'version': 21, 'width': 101, 'maxChar': 1352},
                    {'version': 22, 'width': 105, 'maxChar': 1460},
                    {'version': 23, 'width': 109, 'maxChar': 1588},
                    {'version': 24, 'width': 113, 'maxChar': 1704},
                    {'version': 25, 'width': 117, 'maxChar': 1853},
                    {'version': 26, 'width': 121, 'maxChar': 1990},
                    {'version': 27, 'width': 125, 'maxChar': 2132},
                    {'version': 28, 'width': 129, 'maxChar': 2223},
                    {'version': 29, 'width': 133, 'maxChar': 2369},
                    {'version': 30, 'width': 137, 'maxChar': 2520},
                    {'version': 31, 'width': 141, 'maxChar': 2677},
                    {'version': 32, 'width': 145, 'maxChar': 2840},
                    {'version': 33, 'width': 149, 'maxChar': 3009},
                    {'version': 34, 'width': 153, 'maxChar': 3183},
                    {'version': 35, 'width': 157, 'maxChar': 3351},
                    {'version': 36, 'width': 161, 'maxChar': 3537},
                    {'version': 37, 'width': 165, 'maxChar': 3729},
                    {'version': 38, 'width': 169, 'maxChar': 3927},
                    {'version': 39, 'width': 173, 'maxChar': 4087},
                    {'version': 40, 'width': 177, 'maxChar': 4296}]

    qr = qrcode.QRCode()
    qr.add_data(QR_DATA)
    qr_matrix = qr.get_matrix()

    qr_width = len(qr_matrix)
    print(qr_width)

    dwg = svgwrite.Drawing('qr_output.svg', size=(
        f"{qr_width}mm", f"{qr_width}mm"))
    dwg.add(dwg.rect(insert=("0.5mm", "0.5mm"),
                     size=(f"{qr_width-1}mm", f"{qr_width-1}mm"),
                     rx=BORDER_RADIUS, ry=BORDER_RADIUS,
                     stroke_width="1mm",
                     stroke=BORDER_COLOUR,
                     fill=BORDER_BACKGROUND_COLOUR))

    for row_idx, x in enumerate(qr_matrix):
        for column_idx, y in enumerate(x):
            if 10 < column_idx < qr_width-12:
                if y:
                    dwg.add(dwg.rect(insert=(f"{column_idx}mm", f"{row_idx}mm"),
                                     size=("0.9mm", "0.9mm"),
                                     fill=POSITION_DETECTION_COLOUR,
                                     rx="30", ry="30"))
            else:
                if row_idx > qr_width-13 and column_idx > qr_width - 13:
                    if y:
                        dwg.add(dwg.rect(insert=(f"{column_idx}mm", f"{row_idx}mm"),
                                         size=("0.9mm", "0.9mm"),
                                         fill=POSITION_DETECTION_COLOUR,
                                         rx="30", ry="30"))
                else:
                    if 10 < row_idx < qr_width-12:
                        if y:
                            dwg.add(dwg.rect(insert=(f"{column_idx}mm", f"{row_idx}mm"),
                                             size=("0.9mm", "0.9mm"),
                                             fill=POSITION_DETECTION_COLOUR,
                                             rx="30", ry="30"))

    dwg.add(dwg.rect(insert=(f"4.5mm", f"4.5mm"),
                     size=("6mm", "6mm"),
                     rx=POSITION_DETECTION_RADIUS, ry=POSITION_DETECTION_RADIUS,
                     stroke_width="1mm",
                     stroke=POSITION_DETECTION_COLOUR,
                     fill="white"))
    dwg.add(dwg.rect(insert=(f"6mm", f"6mm"),
                     size=("3mm", "3mm"),
                     fill=POSITION_DETECTION_COLOUR,
                     rx=2.79, ry=2.79,
                     ))

    dwg.add(dwg.rect(insert=(f"{qr_width-11}.5mm", f"4.5mm"),
                     size=("6mm", "6mm"),
                     rx=POSITION_DETECTION_RADIUS, ry=POSITION_DETECTION_RADIUS,
                     stroke_width="1mm",
                     stroke=POSITION_DETECTION_COLOUR,
                     fill="white"))
    dwg.add(dwg.rect(insert=(f"{qr_width-9}mm", f"6mm"),
                     size=("3mm", "3mm"),
                     fill=POSITION_DETECTION_COLOUR,
                     rx=2.79, ry=2.79,
                     ))

    dwg.add(dwg.rect(insert=(f"4.5mm", f"{qr_width-11}.5mm"),
                     size=("6mm", "6mm"),
                     rx=POSITION_DETECTION_RADIUS, ry=POSITION_DETECTION_RADIUS,
                     stroke_width="1mm",
                     stroke=POSITION_DETECTION_COLOUR,
                     fill="white"))
    dwg.add(dwg.rect(insert=(f"6mm", f"{qr_width-9}mm"),
                     size=("3mm", "3mm"),
                     fill=POSITION_DETECTION_COLOUR,
                     rx=2.79, ry=2.79,
                     ))

    dwg.save()

    svg_code = open("qr_output.svg", 'rt').read()
    output_size = 5096
    svg2png(bytestring=svg_code, write_to='qr_output.png',
            output_width=output_size, output_height=output_size)


if __name__ == "__main__":
    gen_qr("https://instagram.com/bongzy")
