#!/usr/bin/env python3


def generate_curved_svg_text(
    text: str,
    width: float = 800,
    arc_height: float | None = None,
    radius: float | None = None,
    text_color: str = "#111",
    text_size: int = 50,
    font_weight: int | str = 300,
    font_family: str = "Gill Sans, 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif"
) -> str:
    """
    Generate an SVG string with text arranged along an arc or circle.

    Parameters
    ----------
    text : str
        The text to display.
    width : float
        The horizontal span of the arc (ignored if radius is given).
    arc_height : float | None
        The vertical rise of the arc (only used for arc mode).
        If None and radius not given, defaults to 0.3 * width.
    radius : float | None
        If provided, text will follow a circular arc of given radius (in px).
        Centered horizontally.
    text_color : str
        SVG color for the text.
    text_size : int
        Font size in px.
    font_weight : int | str
        Font weight (e.g., 300, 400, 'bold').
    font_family : str
        Font family CSS string.
    """
    # If using a circular path
    if radius is not None:
        # Define a circle path centered at mid of width, upward arc
        path_d = f"M {width/2 - radius} 0 A {radius} {radius} 0 0 1 {width/2 + radius} 0"
    else:
        # Default arc shape
        if arc_height is None:
            arc_height = 0.3 * width
        path_d = f"M 0 0 Q {width/2} {-arc_height} {width} 0"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{text_size * 8/3}" viewBox="0 {-text_size*5} {width} {text_size*8}">
  <defs>
    <path id="arc" d="{path_d}" />
  </defs>

  <text font-size="{text_size}"
        font-family="{font_family}"
        font-weight="{font_weight}"
        fill="{text_color}">
    <textPath href="#arc" startOffset="50%" text-anchor="middle">
      {text}
    </textPath>
  </text>
</svg>"""
    return svg


def generate_curved_svg(fname: str, **kwargs) -> None:
    """
    Generate an SVG file with text arranged along an arc or circle.

    Parameters
    ----------
    fname : str
        Output SVG file name.
    **kwargs
        Arguments passed to `generate_curved_svg_text`.
    """
    svg_content = generate_curved_svg_text(**kwargs)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG saved to {fname}")
