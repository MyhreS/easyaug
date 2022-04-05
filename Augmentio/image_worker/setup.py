from setuptools import setup

setup(
    name='image_worker',
    version='1.0',
    packages=['image_worker', 'image_worker.augment', 'image_worker.quickview, image_worker.preprocess'],
    url='',
    license='',
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
