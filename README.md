# Text Arcs

Generate SVG files with curved text for use in e.g. Keynote presentations.

## Installation

Install the package in development mode:

```bash
pip install -e .
```

Or install from source:

```bash
pip install .
```

## Usage

### Command Line

After installation, you can use the `text-arc` command:

```bash
text-arc output.svg "Hello World" --width 800 --arc_height 200 --text_size 50
```

#### Options

- `fname`: Output SVG file name (required)
- `text`: The text to display (required)
- `--width`: Width of the arc (default: 800)
- `--arc_height`: Height of the arc (default: 0.3 \* width)
- `--radius`: Radius for circular arc (overrides arc_height)
- `--text_color`: Color of the text (default: "#111")
- `--text_size`: Font size in px (default: 50)
- `--font_weight`: Font weight (default: "300")
- `--font_family`: Font family (default: "Gill Sans, 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif")

### Python API

You can also use the package in your Python code:

```python
from text_arcs import generate_curved_svg, generate_curved_svg_text

# Generate SVG file
generate_curved_svg(
    fname="output.svg",
    text="Hello World",
    width=800,
    arc_height=200,
    text_size=50
)

# Get SVG string
svg_string = generate_curved_svg_text(
    text="Hello World",
    width=800,
    arc_height=200,
    text_size=50
)
```

## License

MIT
