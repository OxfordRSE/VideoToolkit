# VideoToolkit

A Python toolkit for generating video elements (PDF slides and PNG images) for use in lecture videos and screen recording software like OBS.

⚠️ **Status: Work in Progress** — Development is stalled. Currently supports basic PDF slide generation and PDF-to-PNG conversion. Full video element generation with screen/video cutouts is not yet implemented.

## Current Features

- **PDF Slide Generation**: Create start and end slides with customizable titles and hexagonal grid backgrounds
- **PDF to PNG Conversion**: Convert generated PDFs to PNG format using ImageMagick

## What's Missing

- Video element compositing with screen and video cutouts
- Advanced slide layout and design templates
- Batch processing utilities
- Complete test coverage

## Installation

### External Dependencies

Before installing this package, install:

1. **ImageMagick** (v6.x or v7.x) — https://imagemagick.org/
2. **Ghostscript** — https://www.ghostscript.com/

### Python Package

```bash
pip install -e .
```

## Quick Start

```python
from videotoolkit import create_start_slide, pdf_to_png

# Create a PDF slide
create_start_slide("slide.pdf", "My Lecture Title", "Introduction")

# Convert to PNG
pdf_to_png("slide.pdf")
```

See `scripts/example_script.py` for more examples.
