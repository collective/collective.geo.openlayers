# -*- coding: utf-8 -*-
import unittest
from zope.interface import directlyProvides
from Products.CMFCore.utils import getToolByName

from ..browser.interfaces import IOpenlayers
from ..testing import CGEO_OPENLAYERS_INTEGRATION


class TestSetup(unittest.TestCase):
    layer = CGEO_OPENLAYERS_INTEGRATION

    def setUp(self):
        self.portal = self.layer['portal']
        self.cat = getToolByName(self.layer['portal'], 'portal_catalog')

        self.request = self.layer['request']
        # marking the request with BrowserLayer
        directlyProvides(self.request, IOpenlayers)

    def get_resource(self, name):
        return self.portal.restrictedTraverse(
            name, None
        )

    def test_portal_skins(self):
        skins = getToolByName(self.portal, 'portal_skins')
        layer = skins.getSkinPath('Plone Default')
        self.assertIn('geo_openlayers', layer)

    def test_portal_skins_openlayers_images_folder(self):
        skins = getToolByName(self.portal, 'portal_skins')
        self.assertIsNotNone(skins['geo_openlayers'].hasObject('img'))

    def test_portal_skins_openlayers_lang_folder(self):
        skins = getToolByName(self.portal, 'portal_skins')
        self.assertIsNotNone(skins['geo_openlayers'].hasObject('theme'))
        self.assertIsNotNone(skins['geo_openlayers'].hasObject('lang'))

    def test_portal_skins_marker_image(self):
        try:
            self.portal.restrictedTraverse('img/marker.png')
        except KeyError:
            self.fail('marker.png image was not found')

    def test_portal_skins_theme_image(self):
        self.assertIsNotNone(
            self.get_resource('theme/default/img/ruler.png')
        )

    def test_portal_skins_translations(self):
        self.assertIsNotNone(
            self.get_resource('lang/de.js')
        )

    def test_resource_js(self):
        self.assertIsNotNone(
            self.get_resource('++resource++proj4js.min.js')
        )

    def test_resource_openlayerscss(self):
        self.assertIsNotNone(
            self.get_resource('++resource++geo-openlayers.css')
        )

    def test_javascript_resources(self):
        pjs = getToolByName(self.portal, 'portal_javascripts')
        resources = [
            ("OpenLayers.js", True),
            ("proj4js-compressed.js", True)
        ]

        for id_, enabled in resources:
            res = pjs.getResource(id_)
            self.assertIsNotNone(res)
            self.assertEqual(enabled, res.getEnabled())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
