# _*_ coding: utf-8 _*_
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-liked',
    version='1.0.2',
    author='Amyth Arora',
    author_email='mail@amythsingh.com',
    packages=find_packages(),
    url='https://github.com/amyth/django-liked',
    license='MIT License',
    description='A django likes app',
    long_description='Django Liked is a generic like dislike application that '\
        'built on django 1.10 using the contenttypes framework to create likes'\
        'for any models in your django project',
    zip_safe=False,
)
