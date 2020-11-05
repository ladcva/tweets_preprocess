import setuptools

setuptools.setup(
	name = 'tweets_preprocess', #this should be unique
	include_package_data=True,
	version = '0.1.0',
	author = 'Le Anh Duc',
	author_email = 'ladcva@yahoo.com',
	description = 'Preprocessing package',
	long_description = '',
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)
