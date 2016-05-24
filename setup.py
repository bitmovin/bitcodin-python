from setuptools import setup

setup(
    name='bitcodin',
    description='Python interface for bitcodin API',
    version='1.6.5',
    author='David Moser, Dominic Miglar',
    author_email='david.moser@bitmovin.net, dominic.miglar@bitmovin.net',
    packages=['bitcodin'],
    include_package_data=True,
    url='https://github.com/bitmovin/bitcodin-python',
    install_requires=[
        'requests>=2.4.3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)

