var size = new OpenLayers.Size(15,17);
var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
var icon = new OpenLayers.Icon('./img/marker.png',size,offset);

OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {                
    defaultHandlerOptions: {
        'single': true,
        'double': false,
        'pixelTolerance': 0,
        'stopSingle': false,
        'stopDouble': false
    },

    initialize: function(options) {
        this.handlerOptions = OpenLayers.Util.extend(
            {}, this.defaultHandlerOptions
        );
        OpenLayers.Control.prototype.initialize.apply(
            this, arguments
        ); 
        this.handler = new OpenLayers.Handler.Click(
            this, {
                'click': this.trigger
            }, this.handlerOptions
        );
    }, 

    trigger: function(e) {
        var lonlat = map.getLonLatFromViewPortPx(e.xy) // get spherical mercator coord
        // add a marker to map
        markers.addMarker(new OpenLayers.Marker(lonlat,icon));
        
        // tranform to displayProjection: new OpenLayers.Projection("EPSG:4326")
        lonlat.transform(map.projection, map.displayProjection);

        // popolating the widgets
        document.getElementById(latitude_widget_id).value = lonlat.lat;
        document.getElementById(longitude_widget_id).value = lonlat.lon;
    }

});

var markers = new OpenLayers.Layer.Markers( "Markers" );
map.addLayer(markers);

var click = new OpenLayers.Control.Click();
map.addControl(click);
click.activate();