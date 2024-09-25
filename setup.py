from setuptools import setup, find_packages

setup(
    name='pylookup-tool',
    version='0.1',
    description='A CLI tool for WHOIS Lookup Operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hatix Ntsoa',
    author_email='hatixntsoa@gmail.com',
    url='https://github.com/h471x/whois_lookup',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pylookup=pylookup.main:main',
            'pylookup-gui=pylookup.app.gui:main',
        ],
    },
)