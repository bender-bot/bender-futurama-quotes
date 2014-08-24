from setuptools import setup

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Topic :: Utilities',
]
py_versions = ['2', '2.6', '2.7']
classifiers += ['Programming Language :: Python :: %s' % x for x in py_versions]

setup(
    name='bender-futurama-quotes',
    description='bender-futurama-quotes: random quotes from futurama',
    version='0.1.0',
    url='https://github.com/bender-bot/bender-futurama-quotes',
    license='MIT license',
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
    author='Bruno Oliveira',
    author_email='nicoddemus@gmail.com',
    classifiers=classifiers,
    install_requires=[],
    py_modules=['bender_futurama_quotes'],
    entry_points={
        'bender_script': [
            'futurama-quotes = bender_futurama_quotes:Quotes',
        ],
    }
)

