from setuptools import setup, find_packages

setup(
    name='project_airlines',

    version='1.0.0',
    author='Afonso Claro, Daniel Jimenez',
    author_email='afonso.p.claro@ubi.pt, daniel.jimenez@ubi.pt',
    description='Análise de tweets sobre companhias aéreas',
    long_description=open('README.md.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ubi-datasciencelabs-students/IACD_Prog_20242025_Grupo9',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        'matplotlib>=3.0.0'
    ],
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
