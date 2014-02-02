Introduction
============

collective.geo.openlayers enables `Openlayers`_ machinery into Plone.

This package registers two javascript files into Plone javascript registry:

1. OpenLayers.js
2. proj4js-compressed.js



.. image:: https://secure.travis-ci.org/collective/collective.geo.openlayers.png
    :target: http://travis-ci.org/collective/collective.geo.openlayers

Found a bug? Please, use the `issue tracker`_.

.. contents:: Table of contents


Requirements
============

* `Plone`_ >= 3


Installation
============

This addon can be installed has any other addons, please follow official
documentation_.


Upgrading
=========

Version 3.0
-----------

If you are upgrading from an older version to 3.0, you may need to run
upgrade steps. To do this, follow these steps:

#. Browse to ``portal_setup`` in the ZMI of your site
#. Click onto the ``Upgrades`` tab
#. Select ``collective.geo.openlayers:default`` from the drop-down list and
   click ``Choose Profile``
#. Observe any available upgrades and click the ``Upgrade`` button if any
   are present.


Integration example
===================

You can include openlayers in a Plone browser page in this way
(for further information about openlayers see
other `openlayers examples`_)::

        <html xmlns="http://www.w3.org/1999/xhtml"
              xmlns:metal="http://xml.zope.org/namespaces/metal"
              xmlns:tal="http://xml.zope.org/namespaces/tal"
              metal:use-macro="here/main_template/macros/master">
          <head>

            <metal:block fill-slot="top_slot"
                  tal:define="dummy python:request.set('disable_border',1);
                              portal_state context/@@plone_portal_state;
                              portal_url portal_state/portal_url" />
            <metal:block metal:fill-slot="javascript_head_slot">
              <!-- optional openlayers translation -->
              <script type="text/javascript"
                  tal:attributes="src string:$portal_url/lang/de.js"></script>
              <script type="text/javascript">
                  OpenLayers.Lang.setCode('de');
              </script>

              <script type="text/javascript">
                  jq(window).bind('load', function() {
                     map = new OpenLayers.Map( 'map');
                     layer = new OpenLayers.Layer.OSM( "Simple OSM Map");
                     map.addLayer(layer);
                     map.setCenter(
                        new OpenLayers.LonLat(-71.147, 42.472).transform(
                            new OpenLayers.Projection("EPSG:4326"),
                            map.getProjectionObject()
                        ), 12
                     );
                  });
              </script>
            </metal:block>
          </head>

          <body>
           <metal:content-core fill-slot="content-core">
             <metal:content-core define-macro="content-core">
                <div id="map" class="olMap" style="width:100%;height: 500px;">
                    <!-- openlayers map -->
                </div>

             </metal:content-core>
           </metal:content-core>
          </body>
        </html>

Updating this package
=====================

When a new version of OpenLayers is released, this package can be updated
accordingly using the following steps, keeping in mind that some paths and URLs
will need adjustment::

    cd ~/collective.geo.openlayers
    cd collective/geo/openlayers/skins/
    #Change URL accordingly
    wget http://openlayers.org/download/OpenLayers-<STABLE VERSION>.tar.gz
    tar xf OpenLayers*.tar.gz
    mv OpenLayers-<STABLE VERSION> OpenLayers
    #Maintain 3rd party files
    mv geo_openlayers/plone3_fix_form_tabbing.js geo_openlayers/proj4js-compressed.js .
    git rm geo_openlayers/* -r
    mkdir geo_openlayers
    #Only select the files we need
    mv OpenLayers/{*.js,*.txt,*.md,img,theme} geo_openlayers/
    mv *.js geo_openlayers/
    git add geo_openlayers/
    #Copy the translation files
    mv OpenLayers/lib/OpenLayers/Lang/*.js geo_openlayers/lang/

    #Edit change note now in history
    vim ~/collective.geo.openlayers/docs/HISTORY.txt
    git commit -a -m "Updated to OpenLayers [version]"


Contributors
============

* Giorgio Borelli - gborelli
* Silvio Tomatis - silviot
* David Beitey - davidjb
* Gerhard Weis - gweis
* Denis Krienbühl - href


.. _Openlayers: http://openlayers.org
.. _Plone: http://plone.org
.. _openlayers examples: http://dev.openlayers.org/releases/OpenLayers-2.12/examples
.. _issue tracker: https://github.com/collective/collective.geo.bundle/issues
.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
