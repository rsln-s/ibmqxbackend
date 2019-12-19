from setuptools import setup

setup(name='variationaltoolkit',
	description='a set of tools wrapping variational forms',
	author='Ruslan Shaydulin',
	author_email='rshaydu@g.clemson.edu',
	packages=['variationaltoolkit'],
    install_requires=['qiskit', 'mpsbackend'],
	zip_safe=False)
