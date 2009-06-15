from Products.Five import BrowserView

import zope.publisher.browser
import zope.app.pagetemplate.viewpagetemplatefile

class Macros(zope.publisher.browser.BrowserView):
    template = zope.app.pagetemplate.viewpagetemplatefile.ViewPageTemplateFile(
        'macros.pt')

    def __getitem__(self, key):
        return self.template.macros[key]

class OpenLayers(BrowserView):
    """ default openlayer view """
