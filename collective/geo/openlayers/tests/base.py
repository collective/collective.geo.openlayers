# from Products.Five import zcml
from Zope2.App import zcml
from Products.Five import fiveconfigure

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup


@onsetup
def setup_product():
    """
       Set up the package and its dependencies.
    """

    fiveconfigure.debug_mode = True
    import collective.geo.openlayers
    zcml.load_config('configuretest.zcml', collective.geo.openlayers)

    fiveconfigure.debug_mode = False


setup_product()
ptc.setupPloneSite(products=['collective.geo.openlayers'])


class OpenlayersTestCase(ptc.PloneTestCase):
    pass


class OpenlayersFunctionalTestCase(ptc.FunctionalTestCase):
    pass
