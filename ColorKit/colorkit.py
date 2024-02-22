# Author: Benjamen M.
from tkinter import colorchooser
import colorsys
import tkinter as tk
from random import randint
import colorsys
import math

# Color piker
class ColorPicker:
    def __init__(self):
        self.color = None

    def rgb(self):
        self.color = colorchooser.askcolor()
        rgb = self.color[0]
        return rgb
    
    def hex(self):
        self.color = colorchooser.askcolor()
        rgb = self.color[0]
        hex = rgb_to_hex(rgb)
        return hex
    
    def hsl(self):
        self.color = colorchooser.askcolor()
        rgb = self.color[0]
        hsl = rgb_to_hsl(rgb)
        return hsl
    
    def cmyk(self):
        self.color = colorchooser.askcolor()
        rgb = self.color[0]
        cmyk = rgb_to_cmyk(rgb)
        return cmyk
    
    
# Color viewer
def ViewColor(color):
    hex = color
    if "#" not in color:
        try:
            color = Color(color).hex()
        except AttributeError:
            pass
            # pass because the color is already in hex or rgb 
    if type(color) == tuple:
        if len(color) != 3:
            raise ValueError("The color must be a tuple with 3 RGB values")
        if type(color[0]) != int or type(color[1]) != int or type(color[2]) != int:
            raise TypeError("The RGB values must be integers")
        if color[0] < 0 or color[0] > 255 or color[1] < 0 or color[1] > 255 or color[2] < 0 or color[2] > 255:
            raise ValueError("The RGB values must be in the range [0, 255]")
        
        hex = rgb_to_hex(color)
        print(hex)

    
    win = tk.Tk()
    win.title("Color Viewer")
    win.geometry("200x100")
    # center window
    win.eval('tk::PlaceWindow . center')

    # window background color
    win.configure(bg=hex)
    win.mainloop()

# Colored print
def Print(text, color):
    # check if the color is a tuple or a string
    if type(color) == tuple:
        r, g, b = color
    # make sure the color is a valid color and it's a string
    elif type(color) == str:
        # this will convert he hex to rgb
        if color[0] == '#':
            r, g, b = hex_to_rgb(color)
        elif color.lower() in Color(color).color_map:
            r, g, b = Color(color).rgb()
        else: 
            raise ValueError("Invalid color")
    
    # print the colored text
    colored_text = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    print(colored_text)

def Error(error_message, bold=False):
    # check if the text should be bold
    if bold:
        colored_text = f"\033[1;38;2;255;0;0mERROR: {error_message}\033[0m"
    else:
        colored_text = f"\033[38;2;255;0;0mERROR: {error_message}\033[0m"

    # print the colored text
    print(colored_text)

def Warning(warning_message, bold=False):
    # check if the text should be bold
    if bold:
        colored_text = f"\033[1;38;2;255;165;0mWARNING: {warning_message}\033[0m"
    else:
        colored_text = f"\033[38;2;255;165;0mWARNING: {warning_message}\033[0m"
    print(colored_text)

def Success(success_message, bold=False):
    # check if the text should be bold
    if bold:
        colored_text = f"\033[1;38;2;0;128;0mSUCCESS: {success_message}\033[0m"
    else:
        colored_text = f"\033[38;2;0;128;0mSUCCESS: {success_message}\033[0m"
    
    # print the colored text
    print(colored_text)

def Info(info_message, bold=False):
    # check if the text should be bold
    if bold:
        colored_text = f"\033[1;38;2;0;0;255mINFO: {info_message}\033[0m"
    else:
        colored_text = f"\033[38;2;0;0;255mINFO: {info_message}\033[0m"

    # print the colored text
    print(colored_text)


# Random color
class RandomColor():
    def __init__(self):
        pass
    # return the hex value of the random color
    def hex(self):
        return "#{:02x}{:02x}{:02x}".format(self.rgb()[0], self.rgb()[1], self.rgb()[2])
    # return the rgb value of the random color
    def rgb(self):
        return (randint(0,255), randint(0,255), randint(0,255))
    # view the random color in a window
    def view(self):
        ViewColor(self.hex())

class Color:
    # color map
    def __init__(self,color):
        # color map with all the colors and their rgb values 
        self.color_map = {
            "red": (255, 0, 0),
            "green": (0, 128, 0),
            "blue": (0, 0, 255),  # Update the RGB values for the "blue" color
            "yellow": (255, 255, 0),
            "orange": (255, 165, 0),
            "purple": (128, 0, 128),
            "pink": (255, 192, 203),
            "brown": (165, 42, 42),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "gray": (128, 128, 128),
            "cyan": (0, 255, 255),
            "magenta": (255, 0, 255),
            "gold": (255, 215, 0),
            "silver": (192, 192, 192),
            "maroon": (128, 0, 0),
            "olive": (128, 128, 0),
            "lime": (0, 255, 0),
            "teal": (0, 128, 128),
            "navy": (0, 0, 128),
            "aqua": (0, 255, 255),
            "fuchsia": (255, 0, 255),
            "lime": (0, 255, 0),
            "teal": (0, 128, 128),
            "navy": (0, 0, 128),
            "aqua": (0, 255, 255),
            "fuchsia": (255, 0, 255),
            "lightpink": (255, 182, 193),
            "lightyellow": (255, 255, 224),
            "lightgreen": (144, 238, 144),
            "lightblue": (173, 216, 230),
            "lightorange": (255, 160, 122),
            "lightpurple": (221, 160, 221),
            "lightbrown": (210, 105, 30),
            "lightgray": (211, 211, 211),
            "lightcyan": (224, 255, 255),
            "lightmagenta": (255, 224, 255),
            "lightgold": (255, 236, 139),
            "lightsilver": (192, 192, 192),
            "lightmaroon": (128, 0, 0),
            "lightolive": (128, 128, 0),
            "lightlime": (0, 255, 0),
            "lightteal": (0, 128, 128),
            "lightnavy": (0, 0, 128),
            "lightaqua": (0, 255, 255),
            "lightfuchsia": (255, 0, 255),
            "lightlime": (0, 255, 0),
            "lightteal": (0, 128, 128),
            "IndianRed": (205, 92, 92),
            "LightCoral": (240, 128, 128),
            "Salmon": (250, 128, 114),
            "DarkSalmon": (233, 150, 122),
            "LightSalmon": (255, 160, 122),
            "Crimson": (220, 20, 60),
            "Red": (255, 0, 0),
            "FireBrick": (178, 34, 34),
            "DarkRed": (139, 0, 0),
            "Pink": (255, 192, 203),
            "LightPink": (255, 182, 193),
            "HotPink": (255, 105, 180),
            "DeepPink": (255, 20, 147),
            "MediumVioletRed": (199, 21, 133),
            "PaleVioletRed": (219, 112, 147),
            "LightSalmon": (255, 160, 122), 
            "Coral": (255, 127, 80),
            "Tomato": (255, 99, 71),
            "OrangeRed": (255, 69, 0),
            "DarkOrange": (255, 140, 0),
            "Orange": (255, 165, 0),
            "Gold": (255, 215, 0),
            "Yellow": (255, 255, 0),
            "LightYellow": (255, 255, 224),
            "LemonChiffon": (255, 250, 205),
            "LightGoldenrodYellow": (250, 250, 210),
            "PapayaWhip": (255, 239, 213),
            "Moccasin": (255, 228, 181),
            "PeachPuff": (255, 218, 185),
            "PaleGoldenrod": (238, 232, 170),
            "Khaki": (240, 230, 140),
            "DarkKhaki": (189, 183, 107),
            "Lavender": (230, 230, 250),
            "Thistle": (216, 191, 216),
            "Plum": (221, 160, 221),
            "Violet": (238, 130, 238),
            "Orchid": (218, 112, 214),
            "Fuchsia": (255, 0, 255),
            "Magenta": (255, 0, 255),  # Duplicate of Fuchsia
            "MediumOrchid": (186, 85, 211),
            "MediumPurple": (147, 112, 219),
            "RebeccaPurple": (102, 51, 153),
            "BlueViolet": (138, 43, 226),
            "DarkViolet": (148, 0, 211),
            "DarkOrchid": (153, 50, 204),
            "DarkMagenta": (139, 0, 139),
            "Purple": (128, 0, 128),
            "Indigo": (75, 0, 130),
            "SlateBlue": (106, 90, 205),
            "DarkSlateBlue": (72, 61, 139),
            "MediumSlateBlue": (123, 104, 238),
            "GreenYellow": (173, 255, 47),
            "Chartreuse": (127, 255, 0),
            "LawnGreen": (124, 252, 0),
            "Lime": (0, 255, 0),
            "LimeGreen": (50, 205, 50),
            "PaleGreen": (152, 251, 152),
            "LightGreen": (144, 238, 144),
            "MediumSpringGreen": (0, 250, 154),
            "SpringGreen": (0, 255, 127),
            "MediumSeaGreen": (60, 179, 113),
            "SeaGreen": (46, 139, 87),
            "ForestGreen": (34, 139, 34),
            "Green": (0, 128, 0),
            "DarkGreen": (0, 100, 0),
            "YellowGreen": (154, 205, 50),
            "OliveDrab": (107, 142, 35),
            "Olive": (128, 128, 0),
            "DarkOliveGreen": (85, 107, 47),
            "MediumAquamarine": (102, 205, 170),
            "DarkSeaGreen": (143, 188, 139),
            "LightSeaGreen": (32, 178, 170),
            "DarkCyan": (0, 139, 139),
            "Teal": (0, 128, 128),
            "Aqua": (0, 255, 255),
            "Cyan": (0, 255, 255),  # Duplicate of Aqua
            "LightCyan": (224, 255, 255),
            "PaleTurquoise": (175, 238, 238),
            "Aquamarine": (127, 255, 212),
            "Turquoise": (64, 224, 208),
            "MediumTurquoise": (72, 209, 204),
            "DarkTurquoise": (0, 206, 209),
            "CadetBlue": (95, 158, 160),
            "SteelBlue": (70, 130, 180),
            "LightSteelBlue": (176, 196, 222),
            "PowderBlue": (176, 224, 230),
            "LightBlue": (173, 216, 230),
            "SkyBlue": (135, 206, 235),
            "LightSkyBlue": (135, 206, 250),
            "DeepSkyBlue": (0, 191, 255),
            "DodgerBlue": (30, 144, 255),
            "CornflowerBlue": (100, 149, 237),
            "RoyalBlue": (65, 105, 225),
            "Blue": (0, 0, 255),
            "MediumBlue": (0, 0, 205),
            "DarkBlue": (0, 0, 139),
            "Navy": (0, 0, 128),
            "MidnightBlue": (25, 25, 112),
            "Cornsilk": (255, 248, 220),
            "BlanchedAlmond": (255, 235, 205),
            "Bisque": (255, 228, 196),
            "NavajoWhite": (255, 222, 173),
            "Wheat": (245, 222, 179),
            "BurlyWood": (222, 184, 135),
            "Tan": (210, 180, 140),
            "RosyBrown": (188, 143, 143),
            "SandyBrown": (244, 164, 96),
            "Goldenrod": (218, 165, 32),
            "DarkGoldenrod": (184, 134, 11),
            "Peru": (205, 133, 63),
            "Chocolate": (210, 105, 30),
            "SaddleBrown": (139, 69, 19),
            "Sienna": (160, 82, 45),
            "Brown": (165, 42, 42),
            "Maroon": (128, 0, 0),
            "White": (255, 255, 255),
            "Snow": (255, 250, 250),
            "HoneyDew": (240, 255, 240),
            "MintCream": (245, 255, 250),
            "Azure": (240, 255, 255),
            "AliceBlue": (240, 248, 255),
            "GhostWhite": (248, 248, 255),
            "WhiteSmoke": (245, 245, 245),
            "SeaShell": (255, 245, 238),
            "Beige": (245, 245, 220),
            "OldLace": (253, 245, 230),
            "FloralWhite": (255, 250, 240),
            "Ivory": (255, 255, 240),
            "AntiqueWhite": (250, 235, 215),
            "Linen": (250, 240, 230),
            "LavenderBlush": (255, 240, 245),
            "MistyRose": (255, 228, 225),
            "Gainsboro": (220, 220, 220),
            "LightGray": (211, 211, 211),
            "Silver": (192, 192, 192),
            "DarkGray": (169, 169, 169),
            "Gray": (128, 128, 128),
            "DimGray": (105, 105, 105),
            "LightSlateGray": (119, 136, 153),
            "SlateGray": (112, 128, 144),
            "DarkSlateGray": (47, 79, 79),
            "Black": (0, 0, 0)
        }
        self.color = color
        # convert the color to lowercase to make it case insensitive
        self.color = color.lower()
    # return the rgb value of the color when the color is called
    def rgb(self):
        if self.color not in self.color_map:
            raise ValueError("Invalid color")
        return self.color_map[self.color]
    # return the hex value of the color when the color is called
    def hex(self):
        if self.color not in self.color_map:
            raise ValueError("Invalid color")
        return "#{:02x}{:02x}{:02x}".format(*self.rgb())
    # return the hsl value of the color when the color is called
    def hsl(self):
        if self.color not in self.color_map:
            raise ValueError("Invalid color")
        r, g, b = self.rgb()
        hsl = rgb_to_hsl((r, g, b)) 
        return tuple(hsl)
    # return the cymk value of the color when the color is called
    def cymk(self):
        if self.color not in self.color_map:
            raise ValueError("Invalid color")
        r, g, b = self.rgb()
        cmyk = rgb_to_cmyk((r, g, b))
        return tuple(cmyk)

# Color conversion
# RGB to hex 
def rgb_to_hex(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    
    r, g, b = rgb  # Assign the values of r, g, and b
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex_to_rgb(hex_color):
    if type(hex_color) != str:
        raise TypeError("The hex color must be a string")
    if len(hex_color) != 7:
        raise ValueError("The hex color must have 7 characters")
    if hex_color[0] != '#':
        raise ValueError("The hex color must start with a #")
    if not all(c in '0123456789abcdefABCDEF' for c in hex_color[1:]):
        raise ValueError("The hex color must contain only hexadecimal characters")
    
    hex_color = hex_color.lstrip('#')
    lv = len(hex_color)
    return tuple(int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# RGB to hsv
def rgb_to_hsv(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    
    r, g, b = rgb

    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    # HSV values are in the range [0, 1], convert hue to degrees
    h = round(h * 360, 2)
    s = round(s * 100, 2)
    v = round(v * 100, 2)
    return (h, s, v)

def hsv_to_rgb(hsv):
    if type(hsv) != tuple:
        raise TypeError("The HSV must be a tuple")
    if len(hsv) != 3:
        raise ValueError("The HSV must have 3 elements")
    if type(hsv[0]) != int or type(hsv[1]) != int or type(hsv[2]) != int:
        raise TypeError("The HSV values must be integers")
    if hsv[0] < 0 or hsv[0] > 360 or hsv[1] < 0 or hsv[1] > 100 or hsv[2] < 0 or hsv[2] > 100:
        raise ValueError("The HSV values must be in the range [0, 360], [0, 100], [0, 100]")

    h, s, v = hsv

    # Convert HSV values to the range [0, 1]
    h, s, v = h / 360.0, s / 100.0, v / 100.0
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    # Convert RGB values back to the range [0, 255]
    return (int(r * 255), int(g * 255), int(b * 255))

# RGB to hsl
def rgb_to_hsl(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    
    r, g, b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b) 
    # Convert to percentages
    hsl = (h * 360, s * 100, l * 100)
    # round the values to 2 decimal places
    return (round(hsl[0], 2), round(hsl[1], 2), round(hsl[2], 2))

def hsl_to_rgb(hsl):
    if type(hsl) != tuple:
        raise TypeError("The HSL must be a tuple")
    if len(hsl) != 3:
        raise ValueError("The HSL must have 3 elements")
    h,s,l = hsl
    if h < 0 or h > 360 or s < 0 or s > 100 or l < 0 or l > 100:
        raise ValueError("The HSL values must be in the range [0, 360], [0, 100], [0, 100]")
    if type(h) != int or type(s) != int or type(l) != int:
        raise TypeError("The HSL values must be integers")
    

    h, s, l = h / 360.0, s / 100.0, l / 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (int(r * 255), int(g * 255), int(b * 255))

# RGB to cmyk
def rgb_to_cmyk(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r, g, b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    
    if (r, g, b) == (0, 0, 0):
        # Black
        return 0, 0, 0, 100

    # RGB [0,255] -> CMY [0,1]
    c = 1 - r / 255.0
    m = 1 - g / 255.0
    y = 1 - b / 255.0

    # Min. value of CMY
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # CMYK [0,1] -> CMYK [0,100]
    c = round(c * 100, 2)
    m = round(m * 100, 2)
    y = round(y * 100, 2)
    k = round(k * 100, 2)

    return c, m, y, k

def cmyk_to_rgb(cmyk):
    if type(cmyk) != tuple:
        raise TypeError("The CMYK must be a tuple")
    if len(cmyk) != 4:
        raise ValueError("The CMYK must have 4 elements")
    if cmyk[0] < 0 or cmyk[0] > 100 or cmyk[1] < 0 or cmyk[1] > 100 or cmyk[2] < 0 or cmyk[2] > 100 or cmyk[3] < 0 or cmyk[3] > 100:
        raise ValueError("The CMYK values must be in the range [0, 100]")
    if type(cmyk[0]) != int or type(cmyk[1]) != int or type(cmyk[2]) != int or type(cmyk[3]) != int:
        raise TypeError("The CMYK values must be integers")
    
    c, m, y, k = cmyk
    # CMYK [0,100] -> CMYK [0,1]
    c, m, y, k = c / 100.0, m / 100.0, y / 100.0, k / 100.0

    # CMYK -> CMY -> RGB
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)

    return int(r), int(g), int(b)

#rgb to yuv
def rgb_to_yuv(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r, g, b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
        
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.147 * r - 0.289 * g + 0.436 * b
    v = 0.615 * r - 0.515 * g - 0.100 * b
    return round(y, 2), round(u, 2), round(v, 2)

def yuv_to_rgb(yuv):
    if type(yuv) != tuple:
        raise TypeError("The YUV must be a tuple")
    if len(yuv) != 3:
        raise ValueError("The YUV must have 3 elements")
    if yuv[0] < 0 or yuv[0] > 255 or yuv[1] < -0.5 or yuv[1] > 0.5 or yuv[2] < -0.5 or yuv[2] > 0.5:
        raise ValueError("The YUV values must be in the range [0, 255], [-0.5, 0.5], [-0.5, 0.5]")
    if not isinstance(yuv[0], (int, float)) or not isinstance(yuv[1], (int, float)) or not isinstance(yuv[2], (int, float)):
        raise TypeError("The YUV values must be integers or floats")
    

    y, u, v = yuv
    r = y + 1.140 * v
    g = y - 0.395 * u - 0.581 * v
    b = y + 2.032 * u
    return int(r), int(g), int(b)

# rgb to yiq
def rgb_to_yiq(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r, g, b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    
    y = 0.299 * r + 0.587 * g + 0.114 * b
    i = 0.596 * r - 0.274 * g - 0.322 * b
    q = 0.211 * r - 0.523 * g + 0.312 * b
    return round(y, 2), round(i, 2), round(q, 2)

def yiq_to_rgb(yiq):
    if type(yiq) != tuple:
        raise TypeError("The YIQ must be a tuple")
    if len(yiq) != 3:
        raise ValueError("The YIQ must have 3 elements")
    if yiq[0] < 0 or yiq[0] > 255 or yiq[1] < -0.5957 or yiq[1] > 0.5957 or yiq[2] < -0.5226 or yiq[2] > 0.5226:
        raise ValueError("The YIQ values must be in the range [0, 255], [-0.5957, 0.5957], [-0.5226, 0.5226]")
    if not isinstance(yiq[0], (int, float)) or not isinstance(yiq[1], (int, float)) or not isinstance(yiq[2], (int, float)):
        raise TypeError("The YIQ values must be integers or floats")
    

    y, i, q = yiq
    r = y + 0.956 * i + 0.621 * q
    g = y - 0.272 * i - 0.647 * q
    b = y - 1.106 * i + 1.703 * q
    return int(r), int(g), int(b)

# rgb to ycbcr
def rgb_to_ycbcr(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements") 
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r, g, b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = 128 - 0.168736 * r - 0.331264 * g + 0.5 * b
    cr = 128 + 0.5 * r - 0.418688 * g - 0.081312 * b
    return round(y, 4), round(cb, 4), round(cr, 4)

def ycbcr_to_rgb(ycbcr):
    if type(ycbcr) != tuple:
        raise TypeError("The YCbCr must be a tuple")
    if len(ycbcr) != 3:
        raise ValueError("The YCbCr must have 3 elements")
    if ycbcr[0] < 0 or ycbcr[0] > 255 or ycbcr[1] < 16 or ycbcr[1] > 240 or ycbcr[2] < 16 or ycbcr[2] > 240:
        raise ValueError("The YCbCr values must be in the range [0, 255], [16, 240], [16, 240]")
    if not isinstance(ycbcr[0], (int, float)) or not isinstance(ycbcr[1], (int, float)) or not isinstance(ycbcr[2], (int, float)):
        raise TypeError("The YCbCr values must be integers or floats")
    
    y, cb, cr = ycbcr
    r = y + 1.402 * (cr - 128)
    g = y - 0.344136 * (cb - 128) - 0.714136 * (cr - 128)
    b = y + 1.772 * (cb - 128)
    return int(r), int(g), int(b)

# rgb to xyz    
def rgb_to_xyz(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r,g,b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    r, g, b = [x / 255.0 for x in rgb]

    r = (r / 12.92) if (r / 12.92) <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4
    g = (g / 12.92) if (g / 12.92) <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4
    b = (b / 12.92) if (b / 12.92) <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4

    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    x = round(x, 5)
    y = round(y, 5)
    z = round(z, 5)

    return x, y, z

def xyz_to_rgb(xyz):
    if type(xyz) != tuple:
        raise TypeError("The XYZ must be a tuple")
    if len(xyz) != 3:
        raise ValueError("The XYZ must have 3 elements")
    if not isinstance(xyz[0], (int, float)) or not isinstance(xyz[1], (int, float)) or not isinstance(xyz[2], (int, float)):
        raise TypeError("The XYZ values must be integers or floats")
    if xyz[0] < 0 or xyz[0] > 100 or xyz[1] < 0 or xyz[1] > 100 or xyz[2] < 0 or xyz[2] > 100:
        raise ValueError("The XYZ values must be in the range [0, 100]")
    
    x, y, z = xyz
    x /= 100
    y /= 100
    z /= 100
    r = x * 3.2404542 + y * -1.5371385 + z * -0.4985314
    g = x * -0.9692660 + y * 1.8760108 + z * 0.0415560
    b = x * 0.0556434 + y * -0.2040259 + z * 1.0572252
    r = 1.055 * (r ** (1 / 2.4)) - 0.055 if r > 0.0031308 else 12.92 * r
    g = 1.055 * (g ** (1 / 2.4)) - 0.055 if g > 0.0031308 else 12.92 * g
    b = 1.055 * (b ** (1 / 2.4)) - 0.055 if b > 0.0031308 else 12.92 * b
    return int(r * 255), int(g * 255), int(b * 255)

# rgb to lab
def rgb_to_lab(rgb):
    # Convert RGB to XYZ without the colorsys module
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r,g,b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    r, g, b = [x / 255.0 for x in rgb]

    # Apply gamma correction to RGB values
    r = (r / 12.92) if (r <= 0.04045) else ((r + 0.055) / 1.055) ** 2.4
    g = (g / 12.92) if (g <= 0.04045) else ((g + 0.055) / 1.055) ** 2.4
    b = (b / 12.92) if (b <= 0.04045) else ((b + 0.055) / 1.055) ** 2.4

    # Convert RGB to XYZ
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    # Normalize XYZ values to the reference white D65
    x = x / 0.950456
    z = z / 1.088754

    # Apply non-linear transformation to XYZ
    x = (x ** (1 / 3)) if (x > 0.008856) else (903.3 * x + 16) / 116
    y = (y ** (1 / 3)) if (y > 0.008856) else (903.3 * y + 16) / 116
    z = (z ** (1 / 3)) if (z > 0.008856) else (903.3 * z + 16) / 116

    # Calculate Lab values
    l = max(0, min(100, 116 * y - 16))
    a = max(-128, min(127, (x - y) * 500))
    b = max(-128, min(127, (y - z) * 200))

    return round(l, 3), round(a, 3), round(b, 3)

def lab_to_rgb(lab):
    if type(lab) != tuple:
        raise TypeError("The LAB must be a tuple")
    if len(lab) != 3:
        raise ValueError("The LAB must have 3 elements")
    if not isinstance(lab[0], (int, float)) or not isinstance(lab[1], (int, float)) or not isinstance(lab[2], (int, float)):
        raise TypeError("The LAB values must be integers or floats")
    if lab[0] < 0 or lab[0] > 100 or lab[1] < -128 or lab[1] > 127 or lab[2] < -128 or lab[2] > 127:
        raise ValueError("The LAB values must be in the range [0, 100], [-128, 127], [-128, 127]")
    
    l, a, b = lab
    y = (l + 16.0) / 116.0
    x = a / 500.0 + y
    z = y - b / 200.0
    x = x ** 3 if x ** 3 > 0.008856 else (x - 16.0 / 116.0) / 7.787
    y = y ** 3 if y ** 3 > 0.008856 else (y - 16.0 / 116.0) / 7.787
    z = z ** 3 if z ** 3 > 0.008856 else (z - 16.0 / 116.0) / 7.787
    x *= 95.047
    y *= 100.000
    z *= 108.883
    x = x * 0.95047
    y = y * 1.00000
    z = z * 1.08883
    r = x * 3.2404542 + y * -1.5371385 + z * -0.4985314
    g = x * -0.9692660 + y * 1.8760108 + z * 0.0415560
    b = x * 0.0556434 + y * -0.2040259 + z * 1.0572252
    r = 1.055 * (r ** (1 / 2.4)) - 0.055 if r > 0.0031308 else 12.92 * r
    g = 1.055 * (g ** (1 / 2.4)) - 0.055 if g > 0.0031308 else 12.92 * g
    b = 1.055 * (b ** (1 / 2.4)) - 0.055 if b > 0.0031308 else 12.92 * b
    return int(r * 255), int(g * 255), int(b * 255)

# RGB to luv
def rgb_to_luv(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r,g,b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    r, g, b = r / 255, g / 255, b / 255
    r = r ** 2.2 if r > 0.04045 else r / 12.92
    g = g ** 2.2 if g > 0.04045 else g / 12.92
    b = b ** 2.2 if b > 0.04045 else b / 12.92
    r *= 100
    g *= 100
    b *= 100
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041
    x /= 95.047
    y /= 100.000
    z /= 108.883
    x = x ** (1 / 3) if x > 0.008856 else 7.787 * x + 16 / 116
    y = y ** (1 / 3) if y > 0.008856 else 7.787 * y + 16 / 116
    z = z ** (1 / 3) if z > 0.008856 else 7.787 * z + 16 / 116
    l = 116 * y - 16
    u = 13 * l * (4 * x / (x + 15 * y + 3 * z) - 0.19793943)
    v = 13 * l * (9 * y / (x + 15 * y + 3 * z) - 0.46831096)
    return l, u, v

def luv_to_rgb(luv):
    if type(luv) != tuple:
        raise TypeError("The LUV must be a tuple")
    if len(luv) != 3:
        raise ValueError("The LUV must have 3 elements")
    if not isinstance(luv[0], (int, float)) or not isinstance(luv[1], (int, float)) or not isinstance(luv[2], (int, float)):
        raise TypeError("The LUV values must be integers or floats")
    if luv[0] < 0 or luv[0] > 100 or luv[1] < -134 or luv[1] > 220 or luv[2] < -140 or luv[2] > 122:
        raise ValueError("The LUV values must be in the range [0, 100], [-134, 220], [-140, 122]")
    
    l, u, v = luv
    y = (l + 16.0) / 116.0
    u = u / (13 * l) + 0.19793943
    v = v / (13 * l) + 0.46831096
    y = y ** 3 if y ** 3 > 0.008856 else (y - 16.0 / 116.0) / 7.787
    x = -1.5 * y * u / v if v != 0 else 0
    z = 3 * y * (1 - u - v) / v if v != 0 else 0
    x *= 95.047
    y *= 100.000
    z *= 108.883
    r = x * 3.2404542 + y * -1.5371385 + z * -0.4985314
    g = x * -0.9692660 + y * 1.8760108 + z * 0.0415560
    b = x * 0.0556434 + y * -0.2040259 + z * 1.0572252
    r = 1.055 * (r ** (1 / 2.4)) - 0.055 if r > 0.0031308 else 12.92 * r
    g = 1.055 * (g ** (1 / 2.4)) - 0.055 if g > 0.0031308 else 12.92 * g
    b = 1.055 * (b ** (1 / 2.4)) - 0.055 if b > 0.0031308 else 12.92 * b
    return int(r * 255), int(g * 255), int(b * 255)

# rgb to lch
def rgb_to_lch(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r,g,b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    r = r ** 2.2 if r > 0.04045 else r / 12.92
    g = g ** 2.2 if g > 0.04045 else g / 12.92
    b = b ** 2.2 if b > 0.04045 else b / 12.92
    r *= 100
    g *= 100
    b *= 100
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041
    x /= 95.047
    y /= 100.000
    z /= 108.883
    x = x ** (1 / 3) if x > 0.008856 else 7.787 * x + 16 / 116
    y = y ** (1 / 3) if y > 0.008856 else 7.787 * y + 16 / 116
    z = z ** (1 / 3) if z > 0.008856 else 7.787 * z + 16 / 116
    l = 116 * y - 16
    a = 500 * (x - y)
    b = 200 * (y - z)
    c = (a ** 2 + b ** 2) ** 0.5
    h = math.degrees(math.atan2(b, a))
    return l, c, h

def lch_to_rgb(lch):
    if type(lch) != tuple:
        raise TypeError("The LCH must be a tuple")
    if len(lch) != 3:
        raise ValueError("The LCH must have 3 elements")
    if not isinstance(lch[0], (int, float)) or not isinstance(lch[1], (int, float)) or not isinstance(lch[2], (int, float)):
        raise TypeError("The LCH values must be integers or floats")
    if lch[0] < 0 or lch[0] > 100 or lch[1] < 0 or lch[1] > 185.98 or lch[2] < 0 or lch[2] > 360:
        raise ValueError("The LCH values must be in the range [0, 100], [0, 185.98], [0, 360]")

    l, c, h = lch
    h = math.radians(h)
    a = math.cos(h) * c
    b = math.sin(h) * c
    return lab_to_rgb((l, a, b))

# rgb to lms
def rgb_to_lms(rgb):
    if type(rgb) != tuple:
        raise TypeError("The RGB must be a tuple")
    if len(rgb) != 3:
        raise ValueError("The RGB must have 3 elements")
    if type(rgb[0]) != int or type(rgb[1]) != int or type(rgb[2]) != int:
        raise TypeError("The RGB values must be integers")
    r,g,b = rgb
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("The RGB values must be in the range [0, 255]")
    
    r, g, b = r / 255, g / 255, b / 255
    l = 0.3811 * r + 0.5783 * g + 0.0402 * b
    m = 0.1967 * r + 0.7244 * g + 0.0782 * b
    s = 0.0241 * r + 0.1288 * g + 0.8444 * b
    return l, m, s

def lms_to_rgb(lms):
    if type(lms) != tuple:
        raise TypeError("The LMS must be a tuple")
    if len(lms) != 3:
        raise ValueError("The LMS must have 3 elements")
    if not isinstance(lms[0], (int, float)) or not isinstance(lms[1], (int, float)) or not isinstance(lms[2], (int, float)):
        raise TypeError("The LMS values must be integers or floats")
    if lms[0] < 0 or lms[0] > 1 or lms[1] < 0 or lms[1] > 1 or lms[2] < 0 or lms[2] > 1:
        raise ValueError("The LMS values must be in the range [0, 1]")
    
    l, m, s = lms
    r = 4.4679 * l - 3.5873 * m + 0.1193 * s
    g = -1.2186 * l + 2.3809 * m - 0.1624 * s
    b = 0.0497 * l - 0.2439 * m + 1.2045 * s
    r = 255 if r > 1 else 0 if r < 0 else r * 255
    g = 255 if g > 1 else 0 if g < 0 else g * 255
    b = 255 if b > 1 else 0 if b < 0 else b * 255
    return int(r), int(g), int(b)
