from setuptools import setup, find_packages

version = '3.1.1'

setup(
    name='plone.keyring',
    version=version,
    description="Manage secrets",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Framework :: Zope2",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        ],
    keywords='',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.org/project/plone.keyring',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'ZODB3',
        'zope.container',
        'zope.interface',
        'zope.location',
    ],
    )
