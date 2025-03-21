from setuptools import setup, find_packages

setup(
	name="SAN",
	version="0.1",
	packages=find_packages(),
	install_requires=[
		"gnuradio"
	]
	entry_points={
		"console_scripts": [
			"spectrum-analyzer=SpectrumAnalyzer:main",

		],
	},
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	long_desctription=open('README.md').read(),
	long_desctription_content_type="text/markdown",
)
