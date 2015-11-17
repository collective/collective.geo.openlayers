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

* `Plone`_ >= 5.0

for previous Plone versions use collective.geo.openlayers < 4.x


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
        <metal:block metal:fill-slot="javascript_head_slot">
          <script type="text/javascript">
            <!--
              (function ($) {
                var map;
                $(window).load(function() {
                  map = new OpenLayers.Map('map',{
                    theme: null
                  });
                  map.addLayer(new OpenLayers.Layer.OSM("OpenStreetMap"));
                  map.setCenter(new OpenLayers.LonLat(7, 45).transform(
                      new OpenLayers.Projection("EPSG:4326"),
                      map.getProjectionObject()
                  ), 5);

                });
              }(jQuery));
            // -->
          </script>
        </metal:block>
      </head>
      <body>
        <metal:content fill-slot="content-core">
            <metal:content define-macro="content-core">
              <div id="map" class="olMap widget-cgmap">
                <!-- openlayers map -->
              </div>
            </metal:content>
        </metal:content>
      </body>
    </html>


Updating this package
=====================

When a new version of OpenLayers is released, the javascript on this package
can be updated by using the Makefile in the root directory. Commands available:

  * build - it builds a new version of OpenLayer javascript.
  * copysrc - it copies all necessary files in plone resources directory.
  * dist - it is the default command, it executes all previous commands.


Contributors
============

See the complete `list of contributors`_ on Github:

* https://github.com/collective/collective.geo.openlayers/graphs/contributors


.. _Openlayers: http://openlayers.org
.. _Plone: http://plone.org
.. _openlayers examples: http://dev.openlayers.org/releases/OpenLayers-2.12/examples
.. _issue tracker: https://github.com/collective/collective.geo.bundle/issues
.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
.. _list of contributors: https://github.com/collective/collective.geo.openlayers/graphs/contributors
