try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    "description": "My second test project ex47 project",
    "install_requires": ["nose"],
    "packages":["ex47"],
    "scripts":[],
    "name":"ex47",

}

setup(**config)
