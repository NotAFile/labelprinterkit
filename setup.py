from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    README_TEXT = readme.read()

setup(
    name="labelprinterkit",
    description="A library for creating and printing labels",
    use_scm_version=True,
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    url="https://git.scc.kit.edu/scc-net/labelprinterkit",
    author="Adrian Tschira",
    author_email="packages@notafile.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license='Apache License, Version 2.0',
    keywords='',
    packages=find_packages(where='labelprinterkit/*'),
    install_requires=[
        'pillow',
        'pyusb',
        'packbits',
    ],
    setup_requires=[
        'setuptools_scm'
    ],
    python_requires='>=3.4'
)
