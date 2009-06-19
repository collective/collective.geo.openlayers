Introduction
============

collective.geo.openlayers enables openlayers machinery into Plone.

Requirements
------------
* plone >= 3.2.1

Installation
============
Just a simple easy_install collective.geo.openlayers is enough.

Alternatively, buildout users can install collective.geo.openlayers as part of a specific project's buildout, by having a buildout configuration such as: ::

        [buildout]
        ...
        eggs = 
            zope.i18n>=3.4
            collective.geo.openlayers
        ...
        [instance]
        ...
        zcml = 
            collective.geo.openlayers

Install this product from the Plone control panel.

Contributors
============

* Giorgio Borelli - gborelli
* Silvio Tomatis - silviot

