# Copyright (c) 2024 University of Oxford
#
# This source code is licensed under the MIT License found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path
import tempfile

import videotoolkit


def test_create_start_slide():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Convert the temporary directory path to a Path object
        temp_path = Path(temp_dir)

        pdf_file = temp_path / 'test.pdf'
        png_file = temp_path / 'test.png'

        videotoolkit.create_start_slide(str(pdf_file), 'title', 'subtitle')
        videotoolkit.pdf_to_png(temp_path / 'test.pdf')

        assert pdf_file.is_file()
        assert png_file.is_file()


def test_create_end_slide():
    """Placeholder test for create_end_slide"""
    assert True  # Replace with real test later


def test_magick_command():
    assert videotoolkit.MAGICK_COMMAND == 'magick' or videotoolkit.MAGICK_COMMAND == 'convert'
