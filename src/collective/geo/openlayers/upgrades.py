default_profile = 'profile-collective.geo.openlayers:default'


def upgrade_to_30(context):
    """this upgrade registers Openlayer.js in portal_javascript registry
    """
    context.runImportStepFromProfile(default_profile, 'jsregistry')
