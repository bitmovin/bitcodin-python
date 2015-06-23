from distutils.core import setup

setup(
    #Application name:
    name='bitcodin',

    #Version number (initial):
    version='0.1.0',

    author='David Moser',
    author_email='david.moser@bitmovin.net',

    packages=['bitcodin'],

    include_package_data=True,

    url='http://pypi.python.org/pypi/bitcodin_v010',

    description='Python interface for bitcodin API',

    install_requires=[
        'requests==2.4.3'
    ]
)