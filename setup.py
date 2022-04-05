from setuptools import setup, find_packages

setup(
    name='easyaug',
    homepage='https://github.com/MyhreS/easyaug.git',
    version='1.0',
    packages=find_packages(),
    author='Simon Myhre',
    author_email='simonmyhre1@gmail.com',
    description='A package to fast and easy view, prepare and augment images',
    install_requires=[
        'imageio',
        'matplotlib',
        'numpy',
        'imgaug',
    ]
)

