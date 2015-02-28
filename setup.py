#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-admin-help',
    version="0.1",
    author='Kamil Selwa',
    author_email='selwak@gmail.com',
    description='Interactive help for django admin',
    url='https://github.com/k1000/django-admin-help',
    install_requires=[
        'django',
        'django_admin_bootstrapped',
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)