from setuptools import setup, find_packages
from datetime import datetime
seconds = round((datetime.now() - datetime(2017, 5, 31)).total_seconds())


requires = []
with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='scrolls',
    version='0.0.'+str(seconds),
    description='Log manager.',
    url='https://github.com/ilogue/scrolls',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Jasper J.F. van den Bosch',
    author_email='japsai@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    test_suite="test",
    entry_points={
        'console_scripts': ['scrolls=scrolls.entrypoint:main'],
        'paste.app_factory': ['main = scrolls.server:main']
    }
)
