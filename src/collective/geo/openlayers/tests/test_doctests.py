import unittest
import doctest

from plone.testing import layered
from ..testing import CGEO_OPENLAYERS_FUNCTIONAL


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(
            doctest.DocFileSuite(
                'README.txt',
                package='collective.geo.openlayers',
            ),
            layer=CGEO_OPENLAYERS_FUNCTIONAL
        ),
    ])
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
