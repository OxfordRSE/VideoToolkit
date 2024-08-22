# Copyright (c) 2024 University of Oxford
#
# This source code is licensed under the MIT License found in the
# LICENSE file in the root directory of this source tree.

from .tools import create_start_slide, create_end_slide
from .utils import add_logo, generate_hex_grid, pdf_to_png


import logging
import subprocess

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def detect_imagemagick_command():
    """
    Determine whether the appropriate ImageMagick command is `magick` (v7.x) or `convert` (v6.x).
    :return: either `magick` or `convert` or, if not detected, `None`
    """

    magick_command = None

    try:
        result = subprocess.run(['magick', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0 and 'ImageMagick' in result.stdout:
            magick_command = 'magick'
    except (Exception,):
        pass

    if magick_command:
        return magick_command

    try:
        result = subprocess.run(['convert', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0 and 'ImageMagick' in result.stdout:
            magick_command = 'convert'
    except (Exception,):
        pass

    if magick_command:
        return magick_command

    logger.warning(f'Could not detect ImageMagick either as `magick` or `convert`. Some functionality will not work.')
    return None


MAGICK_COMMAND = detect_imagemagick_command()
logger.info(f'ImageMagick command detected as {MAGICK_COMMAND}')


__all__ = ['create_start_slide', 'create_end_slide', 'add_logo', 'generate_hex_grid', 'pdf_to_png', MAGICK_COMMAND]
