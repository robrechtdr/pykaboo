#from distutils.core import setup
from setuptools import setup

setup(
    name='Pykaboo',
    version='0.1.0',
    author='Robrecht De Rouck',
    author_email='Robrecht.De.Rouck@gmail.com',
    packages=['pykaboo', ],
    #include_package_data=True,
    #scripts= None, #'pykaboo/__init__.py',
    url='http://pypi.python.org/pypi/Pykaboo/',
    license='LICENSE.txt',
    package_data={'': ['pykaboo_style.css']},
    data_files=[('pykaboo',['pykaboo/pykaboo_style.css'])],
    entry_points={
    'console_scripts': ['pykaboo = pykaboo:main', ],},
    description='A python source viewer.',
    long_description=open('README.rst').read(),
    install_requires=[
        "pygments >= 1.5",
    ],
)

#entry_points="""[console_scripts]pykaboo = pykaboo:main"""
