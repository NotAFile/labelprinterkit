from setuptools import setup, find_packages


setup(
    name="labelprinterkit",
    version="0.0.1",
    description="A library for creating and printing labels",
    long_description_content_type="text/markdown",
    url="https://git.scc.kit.edu/scc-net/labelprinterkit",
    author="Adrian Tschira",
    author_email="nota@notafile.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='',
    packages=find_packages(where='labelprinterkit/*'),
    install_requires=[
        'pillow',
        'pyusb',
        'packbits',
    ],
)
