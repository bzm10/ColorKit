from setuptools import setup, find_packages

VERSION = '0.0.1'

DESCRIPTION = 'Python advanced color package'

# Setting up
setup(
    name="ColorKit",
    version=VERSION,
    author="Benjamin Mark",
    author_email="bzmarkovits@yahoo.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=["color conversion", "RGB", "HEX", "CMYK", "HSL", "LAB", "LUV", "XYZ", "YIQ", "HSV", "YUV", "YCbCr", "LCH", "LMS", "color toolkit", "color space", "Python color", "color manipulation", "color analysis", "color utility","python","color"],
    classifiers=[
        "Development Status :: 1 - Released",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
