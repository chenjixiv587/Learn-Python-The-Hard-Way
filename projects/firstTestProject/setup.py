try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    "description": "My first project",
    "author": "BruceChen",
    "url": "no",
    "download_url": "no",
    "author_email": "12365@gmail.com",
    "version": "0.1",
    "install_requires": ["pytest"],
    "packages": ["firstTestProject"],
    "scripts": [],
    "name": "projectname"
}

setup(**config)
