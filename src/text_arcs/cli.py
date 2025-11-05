#!/usr/bin/env python3
"""Command-line interface for text-arcs."""

import argparse
from .core import generate_curved_svg


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate SVG with curved text.")
    parser.add_argument("fname", type=str, help="Output SVG file name.")
    parser.add_argument("text", type=str, help="The text to display.")
    parser.add_argument("--width", type=float, default=800,
                        help="Width of the arc.")
    parser.add_argument("--arc_height", type=float,
                        default=None, help="Height of the arc.")
    parser.add_argument("--radius", type=float, default=None,
                        help="Radius for circular arc.")
    parser.add_argument("--text_color", type=str,
                        default="#111", help="Color of the text.")
    parser.add_argument("--text_size", type=int,
                        default=50, help="Font size in px.")
    parser.add_argument("--font_weight", type=str,
                        default="300", help="Font weight.")
    parser.add_argument("--font_family", type=str,
                        default="Gill Sans, 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
                        help="Font family.")

    args = parser.parse_args()

    generate_curved_svg(
        fname=args.fname,
        text=args.text,
        width=args.width,
        arc_height=args.arc_height,
        radius=args.radius,
        text_color=args.text_color,
        text_size=args.text_size,
        font_weight=args.font_weight,
        font_family=args.font_family
    )


if __name__ == "__main__":
    main()
