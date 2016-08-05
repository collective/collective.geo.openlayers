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


* `Plone`_ >= 3 and < 5.0 for collective.geo.openlayers version 3.x
* `Plone`_ >= 5.0 for collective.geo.openlayers version 4.x


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

There are no new versions of openlayers 2, we need to build our own from master branch of the ol2 respository.

1. Goto skins directory of this package
2. Download latest master from github `wget https://github.com/openlayers/ol2/archive/master.zip`
3. `unzip master.zip`
4. Install closure-compiler.jar (Check Openalayers Readme)
5. Build Openlayers.js, Openlayers.debug.js, Openlayers.mobile.js, Openlayers.mobile.debug.js, Openlayers.light.js, Openlayers.light.debug.js

    - `python build.py -c closure full OpenLayers.js`
    - `python build.py -c none full OpenLayers.debug.js`
    - `python build.py -c closure mobile OpenLayers.mobile.js`
    - `python build.py -c none mobile OpenLayers.mobile.debug.js`
    - `python build.py -c closure light OpenLayers.light.js`
    - `python build.py -c none light OpenLayers.light.debug.js`

6. Move them to skins/geo_openlayers
7. Copy `img` and `theme` files to skins/geo_openlayers
8. Copy `lib/Openlayers/Lang/*` to skins(geo_openlayers/lang)
9. Commit changes, please include hash of Openlayers commit you've used to build ol2.

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
