from setuptools import setup, find_packages
import os

version = '2.5'

setup(name='collective.geo.openlayers',
      version=version,
      description="openlayers support for Plone",
      long_description=open(
          "README.rst").read() + "\n" + open(
              os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Framework :: Plone",
          "Topic :: Internet",
          "Topic :: Scientific/Engineering :: GIS",
          "Programming Language :: Python",
      ],
      keywords='Zope Plone GIS KML Google Maps Bing Yahoo OpenLayers',
      author='Giorgio Borelli',
      author_email='giorgio@giorgioborelli.it',
      url='https://github.com/collective/collective.geo.openlayers',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.geo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFCore',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
