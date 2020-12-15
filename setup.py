from setuptools import setup
import create_license

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name=create_license.PROGRAM_NAME,
	version=create_license.PROGRAM_VERSION,
	packages=['create_license'],
	url=create_license.PROGRAM_URL,
	license='Mozilla Public License version 2.0',
	author=create_license.PROGRAM_AUTHOR,
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
