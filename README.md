# Image Color Replacement Script

This Python script processes all PNG files in the current directory, replacing a specified target color with a default replacement color (white). It utilizes the [Pillow](https://pillow.readthedocs.io/en/stable/) library for image manipulation.

## Features

- **Color Replacement**: Replaces a specific color in PNG images with another color (default is white).
- **Batch Processing**: Automatically processes all PNG files in the current directory.

## Requirements

- **Python 3.x**
- **Pillow**: Python Imaging Library (PIL) fork for image processing.

## Installation

1. **Install Python**: Ensure Python 3 is installed on your system. You can download it from the [official Python website](https://www.python.org/).

2. **Install Pillow**: Install the Pillow library using `pip`:

   ```bash
   pip install pillow
   ```

   For more detailed installation instructions, refer to the [Pillow installation guide](https://pillow.readthedocs.io/en/stable/installation.html).

## Usage

1. **Prepare the Script**: Save the provided script to a `.py` file in the directory containing the PNG images you wish to process.

2. **Run the Script**: Execute the script using a terminal or command prompt:

   ```bash
   python script_name.py
   ```

3. **Input Target Color**: When prompted, enter the hex code of the color you want to replace (e.g., `#FF0000` for red).

4. **Processing**: The script will process each PNG file in the current directory, replacing the specified color with white, and save the modified images with a `processed_` prefix.

### Example

If you want to replace the color red (`#FF0000`) in all PNG files in the current directory, run the script and input `#FF0000` when prompted.

## Functions

- `hex_to_rgb(hex_color)`: Converts a hex color string to an RGB tuple.

- `replace_color(image_path, target_color, replacement_color=(255, 255, 255))`: Replaces a specific color in an image with another color.

- `process_folder(target_hex_color)`: Processes all PNG files in the current folder, replacing the target color with the replacement color.

## Notes

- **Alpha Channel**: The script preserves the alpha channel (transparency) of the images during processing.

- **Default Replacement Color**: The default replacement color is white (`#FFFFFF`). To change this, modify the `replacement_color` parameter in the `replace_color` function.

- **File Naming**: Processed images are saved with a `processed_` prefix to distinguish them from the original files.

## License

This project is licensed under the MIT License. 
