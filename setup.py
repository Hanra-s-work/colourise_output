import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='colourise-output',
    version='1.0.0',
    scripts=['src/colourise_output.py'] ,
    author="Henry Letellier",
    author_email="henrysoftwarehouse@protonmail.com",
    description="A module to help add colour in the terminal using batch colour codes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hanra-s-work/colourise_output",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
