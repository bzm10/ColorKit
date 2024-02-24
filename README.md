# ColorKit

ColorKit is a comprehensive Python library designed for versatile color conversions, manipulations, and more. It simplifies working with various color spaces such as RGB, HEX, CMYK, HSL, LAB, LUV, XYZ, YIQ, HSV, YUV, YCbCr, LCH, and LMS. Whether you're developing applications in web development, data analysis, or scientific computing, ColorKit offers a robust set of tools to enhance your project's color processing capabilities.

With ColorKit, you can easily convert colors between different color spaces, generate random colors, manipulate color palettes, and perform color-related operations. It provides functions to convert colors from one color space to another, generate random colors in different color spaces, print colored text to the terminal, select colors from a color palette, view colors in a window, and more.

ColorKit's extensive documentation provides detailed examples and usage instructions for each color space conversion and feature. It also includes a list of supported color spaces and their corresponding conversion functions. Installation is straightforward using pip, making it easy to integrate ColorKit into your Python projects.

Start leveraging the power of ColorKit to enhance your color processing capabilities in Python today!


## Features

- **Color Space Conversions**: Easily convert between popular and specialized color spaces.
- **Random Color Generator**: Generate random colors in various color spaces.
- **Colored Terminal Outputs/Logs**: Print colored text to the terminal.
- **Color Palette**: Select colors from a color palette.
- **Color Viewer**: View any color in a window.
- **Color Names Converter**: Get the color value from a color name.

## Installation

```bash
pip3 install ColorKit
```

# Documentation

## Color Space Conversions Example

```python
import ColorKit as ck

# Convert RGB to HEX
# NOTE: The RGB values must be in a tuple.
hex_color = ck.rgb_to_hex((255, 0, 0))
# NOTE: The HEX value will be a string.
rgb_color = ck.hex_to_rgb("#FF0000")

# Convert RGB to CMYK
cmyk_color = ck.rgb_to_cmyk((255, 0, 0))
rgb_color = ck.cmyk_to_rgb((0, 1, 1, 0))
```

## You can use the same approach for the following color spaces:

<details>
    <summary>List of color spaces</summary>
    rgb_to_hex,
    hex_to_rgb,
    rgb_to_hsl,
    hsl_to_rgb,
    rgb_to_cmyk,
    cmyk_to_rgb,
    rgb_to_yuv,
    yuv_to_rgb,
    rgb_to_yiq,
    yiq_to_rgb,
    rgb_to_ycbcr,
    ycbcr_to_rgb,
    rgb_to_xyz,
    xyz_to_rgb,
    rgb_to_lab,
    lab_to_rgb,
    rgb_to_luv,
    luv_to_rgb,
    rgb_to_lch,
    lch_to_rgb,
    rgb_to_lms,
    lms_to_rgb,
    rgb_to_hsv,
    hsv_to_rgb,
    rgb_to_hsv,
    hsv_to_rgb,
    rgb_to_xyz
</details>

NOTE: All the color spaces are in the form of tuples (Except HEX).

## Random Color Generator Example

```python
import ColorKit as ck

color = ck.RandomColor()
hex = color.hex()
rgb = color.rgb()

# You can also view the color in a window.
color.view()
```

## Colored Terminal Outputs/Logs Example

To print a log message you can use the folowing code:

```python
from ColorKit import Warning, Error, Success,Info

# Create a warning message in the terminal
Warning("This is a warning message")

# Create an error message in the terminal
Error("This is an error message")

# Create a success message in the terminal
Success("This is a success message")

# Create an info message in the terminal
Info("This is an info message")
```

## Custom Colored Terminal Outputs Example
    
```python
from ColorKit import Print

# Print a message in the terminal with a custom color (HEX, RGB, or color name)
# Make sure you you use Print (with a capital P) instead of print.
Print("This is a custom message", "red")
Print("This is a custom message", "#FF0000")
Print("This is a custom message", (255, 0, 0))
```

## Color Palette Example

```python
import ColorKit as ck

# Open the color palette window and select a color.
picker = ck.ColorPicker()

# Pick the color format the color will be returned in. (RGB/HEX/HSL/CMYK)
color = picker.rgb()

# Then you can use the color as you wish.
# For example, you can print the color to the terminal.
print(color)
```

## Color Viewer Example

```python
from ColorKit import ViewColor

# Select a color to view in a window.
color = (255, 0, 0)

# Open the color viewer window.
ViewColor(color)
```

## Color Names To Color Value Example

```python
import ColorKit as ck

# Get the color value from a color name in a RGB format. (You can also use HEX)
color = ck.Color("red").rgb()
print(color)

# Output: (255, 0, 0)
```
### List of all [available colors](https://github.com/bzm10/ColorKit/blob/main/COLORLIST.md)

# License

ColorKit is released under the MIT License - see the [LICENSE](https://github.com/bzm10/ColorKit/blame/main/LICENSE) file for details.

# Contributing

If you would like to contribute to ColorKit, please read the [CONTRIBUTING.md](https://github.com/bzm10/ColorKit/blob/main/CONTRIBUTING.md)


