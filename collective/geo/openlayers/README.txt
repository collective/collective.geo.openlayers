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

Now, check to make sure the CSS files from OpenLayers are accessible. This causes issues if for the client if they can't be found (eg when the directories aren't registered)

    >>> def loadUrl(url):
    ...    try:
    ...       browser.open(url)
    ...       return True
    ...    except Exception:
    ...       return False

    >>> loadUrl(portal.absolute_url()+'/theme/default/style.css')
    True

    >>> 'div.olMap' in browser.contents
    True

    >>> loadUrl(portal.absolute_url()+'/theme/default/framedCloud.css')
    True

    >>> 'olFramedCloudPopupContent' in browser.contents
    True

    >>> loadUrl(portal.absolute_url()+'/theme/default/ie6-style.css')
    True

    >>> 'olControlZoomPanel' in browser.contents
    True

Check to make sure we can access a given image from OpenLayers

    >>> loadUrl(portal.absolute_url()+'/theme/default/img/editing_tool_bar.png')
    True

    >>> 'PNG' in browser.contents
    True

    >>> browser.open(view_url)
