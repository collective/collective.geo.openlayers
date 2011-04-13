How it work
-----------

we start the tests with the usual boilerplate
    >>> from Testing.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()
    >>> self.portal.error_log._ignored_exceptions = ()

    >>> browser.open(portal_url)

the @@openlayers view must contain a div wrapper for a map
    >>> view_url = '%s/@@openlayers_test' % portal_url
    >>> browser.open(view_url)
    >>> '<div id="map" ' in browser.contents
    True

openlayers javascript
    >>> '<script type="text/javascript" src="http://nohost/plone/OpenLayers.js"></script>' in browser.contents
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
