# -*- coding: utf-8 -*-
import unittest
from ..testing import CGEO_OPENLAYERS_INTEGRATION


class TestSetup(unittest.TestCase):
    layer = CGEO_OPENLAYERS_INTEGRATION

    def setUp(self):
        self.portal = self.layer['portal']

    def get_resource(self, name):
        return self.portal.restrictedTraverse(
            name, None
        )

    def test_openlayers_resource(self):
        self.assertIsNotNone(
            self.get_resource(
                '++plone++openlayers.static/openlayers/OpenLayers.js'
            )
        )

    def test_translations_resource(self):
        self.assertIsNotNone(
            self.get_resource(
                '++plone++openlayers.static/openlayers/Lang/de.js'
            )
        )

    def test_resource_js(self):
        self.assertIsNotNone(
            self.get_resource(
                '++plone++openlayers.static/proj4js-compressed.js'
            )
        )

    def test_resource_openlayerscss(self):
        self.assertIsNotNone(
            self.get_resource(
                '++plone++openlayers.static/geo-openlayers.css'
            )
        )

    def test_javascript_resources(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        self.assertTrue(registry['plone.bundles/openlayers.enabled'])


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
