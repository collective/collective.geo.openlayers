import unittest
from collective.geo.openlayers.tests.base import OpenlayersTestCase
from Products.CMFPlone.utils import getToolByName

from zope.app.publication.interfaces import BeforeTraverseEvent
from plone.browserlayer.layer import mark_layer


class TestSetup(OpenlayersTestCase):

    def afterSetUp(self):
        super(TestSetup, self).afterSetUp()
        # restrictedTraverse does not trigger BeforeTraverseEvent...
        #    so do it manually.
        # TODO: would be better to access these resources with a full
        #       publishing request.
        mark_layer(self.portal, BeforeTraverseEvent(self.portal,
                                                    self.portal.REQUEST))

    def test_portal_skins(self):
        skins = getToolByName(self.portal, 'portal_skins')
        layer = skins.getSkinPath('Plone Default')
        self.failUnless('geo_openlayers' in layer)

    def test_portal_skins_openlayers_images_folder(self):
        skins = getToolByName(self.portal, 'portal_skins')
        layer = skins.getSkinPath('Plone Default')
        self.failUnless('geo_openlayers' in layer)
        self.failUnless(skins['geo_openlayers'].hasObject('img'))

    def test_portal_skins_openlayers_theme_folder(self):
        skins = getToolByName(self.portal, 'portal_skins')
        layer = skins.getSkinPath('Plone Default')
        self.failUnless('geo_openlayers' in layer)
        self.failUnless(skins['geo_openlayers'].hasObject('theme'))

    def test_portal_skins_marker_image(self):
        try:
            self.portal.restrictedTraverse('img/marker.png')
        except KeyError:
            self.fail('marker.png image was not found')

    def test_portal_skins_theme_image(self):
        try:
            self.portal.restrictedTraverse('theme/default/img/ruler.png')
        except KeyError:
            self.fail('ruler.png in default theme not found')

    def test_resource_js(self):
        # bleach -- but to persist is diabolical
        try:
            self.portal.restrictedTraverse('++resource++proj4js.min.js')
        except AttributeError:
            self.fail('++resource++proj4js.min.js resource not found')

    def test_resource_openlayerscss(self):
        # bleach -- but to persist is diabolical
        try:
            self.portal.restrictedTraverse('++resource++geo-openlayers.css')
        except AttributeError:
            self.fail('openlayers.css resource not found')


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
