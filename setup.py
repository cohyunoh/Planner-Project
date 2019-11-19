"""
    This is the setup script for the Flask app.
"""
from distutils.core import setup

setup(name="Planner Flask App",
      version="1.0",
      description="A Planner Built With Flask",
      author="Jun Tao Lei, Connor Oh",
      packages=["flaskr"],
      include_package_data=True,
      url="https://github.com/cohyunoh/Planner-Project.git",
      install_requires=["flask"])
