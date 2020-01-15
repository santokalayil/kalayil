from setuptools import setup, find_packages

with open("README.md",'r') as fh:
	long_description = fh.read()

setup(
	name='santa',
	version='0.1.0', # PEP440
	description='Package for easier Machine Learning Workflow.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	py_modules=['santa'], # by Aus
	package_dir ={'':'src'}, # by Aus.. BUT create a src folder in root foler inside which put my py file
	url='https://github.com/santokalayil/santa',
	author='Santo K Thomas',
	author_email='santokalayil@gmail.com',
	classifiers=[
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.7',
			'Programming Language :: Python :: 3.8',
			'Operating System :: OS Independent'
	],
	)