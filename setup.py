import os
import re
from setuptools import setup, find_packages


def get_file(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    return open(filename)


def find_version(*file_paths):
    f = get_file(*file_paths)
    for line in f:
        if re.match('__version__ = .+', line):
            return re.search('\d.+\d', line).group(0)
    raise RuntimeError('Unable to find string version')


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='teracy-django-html5-boilerplate',
    version=find_version('teracy', 'html5boilerplate', '__init__.py'),
    packages=find_packages(),
    namespace_packages=['teracy'],
    include_package_data=True,
    license='BSD License',
    description='html5-boilerplate Django wrapper application',
    long_description=README,
    url='https://github.com/teracy-official/django-html5-boilerplate',
    author='hoatle',
    author_email='hoatlevan@gmail.com',
    maintainer='hoatle',
    maintainer_email='hoatlevan@gmail.com',
    keywords=['python', 'django', 'html5-boilerplate'],
    install_requires=[
        'django>=1.5'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
    ]
)
