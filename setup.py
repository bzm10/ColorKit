from setuptools import setup, find_packages

VERSION = '0.0.5'

DESCRIPTION = 'A comprehensive Python package for advanced color manipulation and analysis'

# Read the contents of the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    print(fh)
    long_description = fh.read()

# Setting up
setup(
    name="ColorKit",
    version=VERSION,
    author="Benjamin Mark",
    author_email="bzmarkovits@yahoo.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=["color conversion", "RGB", "HEX", "CMYK", "HSL", "LAB", "LUV", "XYZ", "YIQ", "HSV", "YUV", "YCbCr", "LCH", "LMS", "color toolkit", "color space", "Python color", "color manipulation", "color analysis", "color utility","python","color"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license="MIT" 
)
