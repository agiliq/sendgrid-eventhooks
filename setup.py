import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='sendgrid_eventhooks',
    packages=['sendgrid_events'],
    version='0.1.1',
    description='Django app to receive incoming email\
notification events from sendgrid',
    long_description=read("README.md"),
    author='Agiliq Info Solutions',
    author_email='hello@agiliq.com',
    url='https://github.com/agiliq/sendgrid-eventhooks',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
