#!/usr/bin/env python
from PIL import Image
import os

def hex_to_rgb(hex_color):
    """Convert hex color (#RRGGBB) to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def replace_color(image_path, target_color, replacement_color=(255, 255, 255)):
    """Replace a specific color in an image with another color."""
    img = Image.open(image_path).convert('RGBA')  # Ensure the image has an alpha channel
    pixels = img.getdata()

    new_pixels = []
    for pixel in pixels:
        # Match the target color and replace it
        if pixel[:3] == target_color:  # Compare RGB values (ignore alpha)
            new_pixels.append((*replacement_color, pixel[3]))
        else:
            new_pixels.append(pixel)

    img.putdata(new_pixels)
    return img

def process_folder(target_hex_color):
    """Process all PNG files in the current folder."""
    target_rgb_color = hex_to_rgb(target_hex_color)
    png_files = [f for f in os.listdir('.') if f.endswith('.png')]

    for file in png_files:
        print(f"Processing {file}...")
        img = replace_color(file, target_rgb_color)
        img.save(f"processed_{file}")
        print(f"Saved processed_{file}")

if __name__ == "__main__":
    target_hex = input("Enter the hex code of the color to replace (e.g., #FF0000): ").strip()
    process_folder(target_hex)

