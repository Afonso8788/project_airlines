from codecs import open
from setuptools import setup, find_packages
import os

requirementPath = 'requirements.txt.txt'
install_requires = []

if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(
    name="Project_Airlines",
    version="0.1",
    description="Project_Airlines Sentiment Package",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
    },
    author='Afonso Claro'' Daniel Jimenez',
    author_email='daniel.jimenez@ubi.pt''afonso.p.claro@ubi.pt',
    url='https://github.com/ubi-datasciencelabs-students/IACD_Prog_20242025_Grupo9'
)