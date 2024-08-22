# Copyright (c) 2024 University of Oxford
#
# This source code is licensed under the MIT License found in the
# LICENSE file in the root directory of this source tree.

from .tools import create_start_slide, create_end_slide
from .utils import add_logo, generate_hex_grid, pdf_to_png

__all__ = ['create_start_slide', 'create_end_slide', 'add_logo', 'generate_hex_grid', 'pdf_to_png']

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
