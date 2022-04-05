from setuptools import setup, find_packages

setup(
    name='easyaug',
    homepage='',
    version='1.3.4',
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

