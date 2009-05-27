from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='plone.keyring',
      version=version,
      description="Manage secrets",
      long_description=open("README.txt").read() + "\n" + \
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Wichert Akkerman',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.keyring',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
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
