import unittest
from collective.geo.openlayers.tests.base import OpenlayersTestCase
from Products.CMFPlone.utils import getToolByName

class TestSetup(OpenlayersTestCase):
    
    def test_portal_skins(self):
        skins = getToolByName(self.portal, 'portal_skins')
        layer = skins.getSkinPath('Plone Default')
        self.failUnless('geo_openlayers' in layer)

    def test_resource_geopoint_js(self):
        # bleach
        try: 
            self.portal.restrictedTraverse('++resource++geo-point.js')
        except AttributeError:
            self.fail('geo-point.js resource not found')

    def test_resource_geoopenlayers_js(self):
        # bleach -- but to persist is diabolical
        try: 
            self.portal.restrictedTraverse('++resource++geo-openlayers.js')
        except AttributeError:
            self.fail('geo-openlayers.js resource not found')

    def test_resource_openlayerscss(self):
        # bleach -- but to persist is diabolical
        try: 
            self.portal.restrictedTraverse('++resource++openlayers.css')
        except AttributeError:
            self.fail('openlayers.css resource not found')

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
