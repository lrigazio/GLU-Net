import setuptools

with open("dense/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dense",
    version="1.0.0",
    author="Luca Rigazio",
    author_email="luca.rigazio@gmail.com",
    packages=setuptools.find_packages(),
    description="Dense-flow package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/example-pkg",
    license='GPT3',
    python_requires='>=3.6',
    install_requires=[
         "cupy-cuda102==8.3.0",
    ]
)

