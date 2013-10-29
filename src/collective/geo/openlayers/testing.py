# -*- coding: utf-8 -*-
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.geo.openlayers


CGEO_OPENLAYERS = PloneWithPackageLayer(
    zcml_package=collective.geo.openlayers,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.geo.openlayers:default',
    name="CGEO_OPENLAYERS")

CGEO_OPENLAYERS_INTEGRATION = IntegrationTesting(
    bases=(CGEO_OPENLAYERS, ),
    name="CGEO_OPENLAYERS_INTEGRATION")

CGEO_OPENLAYERS_FUNCTIONAL = FunctionalTesting(
    bases=(CGEO_OPENLAYERS, ),
    name="CGEO_OPENLAYERS_FUNCTIONAL")
