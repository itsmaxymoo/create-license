from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='create-license',
	version='2.0.5',
	packages=['create_license'],
	url='https://github.com/itsmaxymoo/create-license',
	license='MIT License',
	author='Max Loiacono',
	author_email='',
	description='Easily create license files.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	entry_points={
		'console_scripts': ['create-license=create_license:main']
	},
	package_data={
		'create_license': ['templates/*.txt']
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6'
)
