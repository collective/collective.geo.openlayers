How it works
------------

we start the tests with the usual boilerplate
    >>> from plone.testing.z2 import Browser
    >>> browser = Browser(layer['app'])
    >>> portal = layer['portal']
    >>> portal_url = portal.absolute_url()
    >>> portal.error_log._ignored_exceptions = ()


the @@openlayers view must contain a div wrapper for a map
    >>> view_url = '%s/@@openlayers_test' % portal_url
    >>> browser.open(view_url)
    >>> '<div id="map" ' in browser.contents
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

Ensure that the translation files can be accessed

    >>> loadUrl(portal.absolute_url()+'/lang/de.js')
    True

