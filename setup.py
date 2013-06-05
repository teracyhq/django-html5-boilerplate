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
    name='vendor-html5boilerplate',
    version=find_version('vendor', 'html5boilerplate', '__init__.py'),
    packages=find_packages(),
    namespace_packages=['vendor'],
    include_package_data=True,
    license='BSD License',
    description='html5-boilerplate Django wrapper application',
    long_description=README,
    url='http://www.teracy.org/projects/vendor-html5boilerplate',
    author='hoatle',
    author_email='hoatlevan@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: html5-boilerplate',
        ],
    )
