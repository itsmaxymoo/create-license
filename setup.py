from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='create-license',
	version='2.0.6',
	packages=['create_license'],
	url='https://github.com/itsmaxymoo/create-license',
	license='Mozilla Public License version 2.0',
	author='Max Loiacono',
	author_email='',
	description='Easily create license files.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	entry_points={
		'console_scripts': ['create-license=create_license:_main']
	},
	package_data={
		'create_license': ['templates/*.txt']
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
		"Operating System :: OS Independent",
	],
	install_requires=[
		"simplecfg"
	],
	python_requires='>=3.6'
)
