from setuptools import setup, find_packages

setup(
    name='easyimgaug',
    version='1.0',
    packages=find_packages('.'),
    package_dir={'': '.'},
    author='Simon Myhre',
    author_email='simonmyhre1@gmail.com',
    description='A package for fast and easy view, prepare and augment images',
    install_requires=[
        'imageio',
        'matplotlib',
        'numpy',
        'imgaug',
        'os',
        'shutil',
        'unittest',
        'glob',
    ]
)
