"""
    This is the setup script for the Flask app.
"""
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="Planner Flask App",
      version="1.0",
      author="Jun Tao Lei, Connor Oh, Leia Park",
      description="A Planner Built With Flask",
      long_description=long_description,
      long_description_content_type="text/markdown"
      url="https://github.com/cohyunoh/Planner-Project.git",
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
      ],
      python_requires=">=3.8")
