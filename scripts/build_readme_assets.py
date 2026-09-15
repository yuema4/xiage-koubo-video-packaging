#!/usr/bin/env python3
"""Build privacy-safe README assets from preview frames."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


TOP_BAND_HEIGHT = 620
BACKGROUND = (8, 17, 29)
LINE = (85, 220, 255)
TEXT = (244, 251, 255)


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def crop_overlay(path: Path, width: int, height: int) -> Image.Image:
    image = Image.open(path).convert("RGB")
    image = image.crop((0, 0, image.width, TOP_BAND_HEIGHT))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def add_caption(image: Image.Image, number: str, label: str, font: ImageFont.ImageFont) -> None:
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 56, image.height), fill=(5, 17, 31))
    draw.text((15, 14), number, fill=LINE, font=font)
    draw.rectangle((56, 0, image.width, 42), fill=(5, 17, 31))
    draw.text((72, 10), label, fill=TEXT, font=font)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--capsule", type=Path, required=True)
    parser.add_argument("--blockframe", type=Path, required=True)
    parser.add_argument("--tech", type=Path, required=True)
    parser.add_argument("--minimal", type=Path, required=True)
    parser.add_argument("--tech-dir", type=Path)
    parser.add_argument("--output", type=Path, default=Path("assets"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    styles = [
        ("01", "CAPSULE", args.capsule, "style-capsule.png"),
        ("02", "BLOCKFRAME", args.blockframe, "style-blockframe.png"),
        ("03", "TECH GLASS", args.tech, "style-tech-glass.png"),
        ("04", "MINIMAL BAR", args.minimal, "style-minimal-bar.png"),
    ]
    label_font = load_font(24)
    heading_font = load_font(36)

    cards = []
    for number, label, source, filename in styles:
        card = crop_overlay(source, 720, 413)
        add_caption(card, number, label, label_font)
        card.save(args.output / filename)
        cards.append(card)

    gap = 22
    margin = 28
    header = 86
    sheet_width = margin * 2 + cards[0].width * 2 + gap
    sheet_height = header + margin * 2 + cards[0].height * 2 + gap
    sheet = Image.new("RGB", (sheet_width, sheet_height), BACKGROUND)
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, 24), "FOUR VIDEO PACKAGING STYLES", fill=TEXT, font=heading_font)
    draw.line((margin, header - 13, sheet_width - margin, header - 13), fill=LINE, width=2)
    positions = [
        (margin, header),
        (margin + cards[0].width + gap, header),
        (margin, header + cards[0].height + gap),
        (margin + cards[0].width + gap, header + cards[0].height + gap),
    ]
    for card, position in zip(cards, positions):
        sheet.paste(card, position)
    sheet.save(args.output / "style-overview.png")

    if args.tech_dir:
        names = [
            "01-hook",
            "03-step-01",
            "04-caption-version-flow",
            "06-subtitle-check",
            "07-step-02",
            "09-output-stack",
            "10-core-rule",
            "11-step-03",
            "12-auto-cards",
            "13-five-minutes",
            "14-human-review",
            "15-card-swap",
            "16-controls",
            "18-step-04",
            "19-auto-align",
            "20-time-comparison",
            "21-automation-quote",
            "22-focus-shift",
            "23-ai-creativity",
            "24-cta",
        ]
        thumb_w, thumb_h = 340, 195
        gap = 16
        margin = 26
        header = 76
        cols = 5
        rows = 4
        width = margin * 2 + cols * thumb_w + (cols - 1) * gap
        height = header + margin * 2 + rows * thumb_h + (rows - 1) * gap
        storyboard = Image.new("RGB", (width, height), BACKGROUND)
        draw = ImageDraw.Draw(storyboard)
        draw.text((margin, 23), "TECH GLASS / 20-FRAME STORYBOARD", fill=TEXT, font=heading_font)
        for index, name in enumerate(names):
            source = args.tech_dir / f"{name}.png"
            thumb = crop_overlay(source, thumb_w, thumb_h)
            x = margin + (index % cols) * (thumb_w + gap)
            y = header + (index // cols) * (thumb_h + gap)
            storyboard.paste(thumb, (x, y))
            draw.rectangle((x, y, x + 54, y + thumb_h), fill=(5, 17, 31))
            draw.text((x + 13, y + 13), f"{index + 1:02d}", fill=LINE, font=label_font)
        storyboard.save(args.output / "tech-glass-storyboard.png")


if __name__ == "__main__":
    main()
