import os
try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))


def get_file_path(relative_path):
	return os.path.join(CURRENT_PATH, relative_path)

README_PATH = get_file_path('README.md')
PROD_REQUIREMENTS = get_file_path("requirements/prod.txt")
TEST_REQUIREMENTS = get_file_path("requirements/test.txt")
HISTORY_PATH = get_file_path('HISTORY.md')

with open(README_PATH) as readme_file:
	readme = readme_file.read()

with open(HISTORY_PATH) as history_file:
	history = history_file.read().replace('.. :changelog:', '')

requirements = [line.strip() for line in open(PROD_REQUIREMENTS)]
test_requirements = [line.strip() for line in open(TEST_REQUIREMENTS)]


setup(
	name='trust_network_backend',
	version='0.1',
	description="Backend for the trust network app",
	long_description=readme + '\n\n' + history,
	author="Ardelean Vlad George",
	author_email='',
	url='https://github.com/vladiibine/trust-network',
	packages=find_packages('src/python/trust_network_backend'),
	package_data={'ty.connect': ['templates/*',  'static/css/*', 'static/js/*', 'static/img/*']},
	include_package_data=True,
	install_requires=requirements,
	zip_safe=False,
	keywords='connect',
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: ISC License (ISCL)',
		'Natural Language :: English',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
	],
	test_suite='tests',
	tests_require=test_requirements,
	entry_points={
		'console_scripts': [
			'tnb_serve=tnb.server:main',
		]
	}
)
