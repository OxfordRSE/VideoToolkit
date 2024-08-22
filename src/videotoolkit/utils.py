# Copyright (c) 2024 University of Oxford
#
# This source code is licensed under the MIT License found in the
# LICENSE file in the root directory of this source tree.

from reportlab.lib import colors
from reportlab.pdfgen import canvas
from math import cos, sin, radians
from pathlib import Path

import logging
import sys
import subprocess

import videotoolkit

logger = logging.getLogger(__name__)


def add_logo(c: canvas.Canvas, logo_path: str, x: float, y: float, width: float, height: float):
    """Adds a logo image to the PDF at the specified position."""
    c.drawImage(logo_path, x, y, width, height)


def generate_hex_grid(c: canvas.Canvas, width: float, height: float, hex_size: float = 30):
    """Generates a hexagonal grid as a background."""
    c.setStrokeColor(colors.blue)
    c.setLineWidth(0.5)

    for y in range(0, int(height), int(hex_size * 1.5)):
        for x in range(0, int(width), int(hex_size * 1.732)):
            if y // (hex_size * 1.5) % 2 == 0:
                draw_hexagon(c, x, y, hex_size)
            else:
                draw_hexagon(c, x + hex_size * 0.866, y, hex_size)


def draw_hexagon(c: canvas.Canvas, x: float, y: float, size: float):
    """Draws a single hexagon centered at (x, y)."""
    points = []
    for i in range(6):
        angle_deg = 60 * i + 30
        angle_rad = radians(angle_deg)
        points.append((x + size * cos(angle_rad), y + size * sin(angle_rad)))

    # To close the hexagon, add the first point to the end of the list
    points.append(points[0])

    # Create the list of line segments
    linelist = [(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1]) for i in range(6)]

    # Draw the hexagon
    c.lines(linelist)


def pdf_to_png(pdf_path: str | Path) -> None:

    if not videotoolkit.MAGICK_COMMAND:
        logger.error(f'ImageMagick not found; required for {__name__}')
        sys.exit(1)

    if isinstance(pdf_path, str):
        pdf_path = Path(pdf_path)

    pdf_path = pdf_path.resolve()

    if not pdf_path.is_file():
        logger.error(f'Path {pdf_path} is not a file. Expected a PDF file.')
        sys.exit(1)

    if pdf_path.suffix != '.pdf':
        logger.error(f'File {pdf_path} is not a PDF file.')

    png_path = pdf_path.with_suffix('.png')

    try:
        # Construct the command to call ImageMagick's convert
        command = [
            videotoolkit.MAGICK_COMMAND,
            '-density', '72',
            str(pdf_path),
            str(png_path)
        ]

        # Execute the command
        subprocess.run(command, check=True)
        logger.info(f'Successfully converted {pdf_path} to {png_path}')

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print("ImageMagick's convert command was not found. Make sure it is installed and accessible.")


