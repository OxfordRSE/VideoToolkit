# Copyright (c) 2024 University of Oxford
#
# This source code is licensed under the MIT License found in the
# LICENSE file in the root directory of this source tree.

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from .utils import add_logo, generate_hex_grid

from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def create_start_slide(filename: str | Path, title: str, subtitle: str):
    """Creates a PDF start slide with the given title and subtitle."""
    # Define the dimensions for a 16:9 aspect ratio
    width, height = 3840, 2160
    # Create a canvas with the specified dimensions
    c = canvas.Canvas(filename, pagesize=(width, height))

    # Draw background grid
    generate_hex_grid(c, width, height)

    # Add title and subtitle
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(width / 2.0, height - 150, title)

    c.setFont("Helvetica", 24)
    c.drawCentredString(width / 2.0, height - 200, subtitle)

    # Save PDF
    c.showPage()
    c.save()
    logger.info(f'Saved {filename}')


def create_end_slide(filename: str, message: str):
    """Creates a PDF end slide with the given message."""
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Draw background grid
    generate_hex_grid(c, width, height)

    # Add message
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(width / 2.0, height - 150, message)

    # Save PDF
    c.showPage()
    c.save()