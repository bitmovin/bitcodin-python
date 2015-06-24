from distutils.core import setup

setup(
    name='bitcodin',
    description='Python interface for bitcodin API',
    version='0.3.0',
    author='David Moser',
    author_email='david.moser@bitmovin.net',
    packages=['bitcodin'],
    include_package_data=True,
    url='https://github.com/bitmovin/bitcodin-python',
    install_requires=[
        'requests==2.4.3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Email',
    ]
)