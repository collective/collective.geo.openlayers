import unittest
import doctest
from Testing import ZopeTestCase as ztc
from collective.geo.openlayers.tests import base


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return unittest.TestSuite([

        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.geo.openlayers',
            test_class=base.OpenlayersFunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | \
                    doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
        ])
