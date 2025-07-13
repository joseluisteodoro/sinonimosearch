from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (name="sinonimosearch",
    version="0.0.1",
    author="jose",
    author_email="joselteodoro2@gmail.com",
    description="buscador de sinonimo",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joseluisteodoro/sinonimosearch/tree/master",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8')
    