from setuptools import setup, find_packages

setup(
    name='project_airlines',

    version='1.0.0',
    author='Afonso Claro, Daniel Jimenez',
    author_email='afonso.p.claro@ubi.pt, daniel.jimenez@ubi.pt',
    description='Análise de tweets sobre companhias aéreas',
    long_description=open('README.md.txt').read(),
    url='https://github.com/ubi-datasciencelabs-students/IACD_Prog_20242025_Grupo9',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    python_requires='>=3.8'
)
