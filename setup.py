from setuptools import setup, find_packages

setup(
    name='shrtcutcli',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'click',
        'beautifulsoup4',
        'random',
        'asyncio'
    ],
    entry_points={
            'console_scripts': ['shrtcut=shrtcutcli:shrtcutcli']
    }
)