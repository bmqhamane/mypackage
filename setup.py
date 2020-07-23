from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/bmqhamane',
    author='<Bukelwa Mqhamane>',
    author_email='<bmqhamane@gmail.com>'
)