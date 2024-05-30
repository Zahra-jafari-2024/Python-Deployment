from setuptools import setup

with open("./README.md", "r") as f:
    long_description = f.read()

with open('./requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name="Edge_Detection_Image",
    version="0.1.0", 
    author="Zahra Jafari", 
    description="image processing technique for finding the boundaries of objects within images",
    long_description=long_description,
    install_requires=install_requires,
    author_email="mzahrajafari94@gmail.com",
    packages=["Edge_Detection_Image"]
)
