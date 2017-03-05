try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages

with open('trust_network_backend/README.md') as readme_file:
	readme = readme_file.read()

with open('trust_network_backend/HISTORY.md') as history_file:
	history = history_file.read().replace('.. :changelog:', '')

requirements = [line.strip() for line in open("trust_network_backend/requirements/prod.txt", 'r')]
test_requirements = [line.strip() for line in open("trust_network_backend/requirements/test.txt", 'r')]


setup(
	name='trust_network_backend',
	version='0.1',
	description="Backend for the trust network app",
	long_description=readme + '\n\n' + history,
	author="Ardelean Vlad George",
	author_email='',
	url='https://github.com/vladiibine/trust-network',
	packages=find_packages(),
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
			'serve=trust_network_backend.server:main',
		]
	}
)
