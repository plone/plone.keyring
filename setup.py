from setuptools import setup, find_packages

version = '2.0b1'

setup(name='plone.keyring',
      version=version,
      description="Manage secrets",
      long_description=open("README.txt").read() + "\n" + \
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Wichert Akkerman',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.keyring',
      license='BSD',
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
