try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup, find_packages

with open('README.md') as readme_file:
	readme = readme_file.read()

with open('HISTORY.md') as history_file:
	history = history_file.read().replace('.. :changelog:', '')

requirements = [line.strip() for line in open('py-requirements/prod.txt')]
test_requirements = [line.strip() for line in open('py-requirements/test.txt')]


def main():
	try:
		import pydevd; pydevd.settrace()
	except ImportError as e:
		pass

	setup(
		name='trust_network_backend',
		version='0.1',
		description="Backend for the trust network app",
		long_description=readme + '\n\n' + history,
		author="Ardelean Vlad George",
		author_email='',
		url='https://github.com/vladiibine/trust-network',
		packages=find_packages('src/python/trust_network_backend'),
		package_data={'tnb': ['templates/*',  'static/css/*', 'static/js/*', 'static/img/*']},
		package_dir={'': 'src/python/trust_network_backend'},
		include_package_data=True,
		install_requires=requirements,
		# include_dirs=[CURRENT_PATH],
		zip_safe=False,
		keywords='trust_network',
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

if __name__ == '__main__':
	main()
