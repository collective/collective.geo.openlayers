collective.geo.openlayers
=========================

Overview
--------
collective.geo.openlayers include openlayers project into Plone.

Tests
-----
we start the tests with the usual boilerplate
    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()
    >>> self.portal.error_log._ignored_exceptions = ()

    >>> from Products.PloneTestCase.setup import portal_owner, default_password
    >>> browser.open(portal_url)

the @@openlayers view must contain a div wrapper for a map
    >>> view_url = '%s/@@openlayers' % portal_url
    >>> browser.open(view_url)
    >>> '<div id="map" ' in browser.contents
    True

openlayers javascript
    >>> '<script type="text/javascript" src="./OpenLayers.js"></script>' in browser.contents
    True

and its css
    >>> '<link href="++resource++openlayers.css" rel="stylesheet" type="text/css" />' in browser.contents
    True
