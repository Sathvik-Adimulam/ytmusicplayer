import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytmusicplayer",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Sathvik Adimulam",                     # Full name of the author
    description="Plays ",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.9',      
    py_modules=["ytmusicplayer"]# Name of the python package
    package_dir={'':'F:\ytmusicplayer'},     # Directory of the source code of the package
    install_requires=["pytube==12.1.0",  "moviepy==1.0.3", "requests==2.28.1"]                     # Install other dependencies if any
)
