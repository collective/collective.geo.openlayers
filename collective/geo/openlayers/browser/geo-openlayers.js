// googlemaps = false;
// lat = 0;
// lon = 0;
// zoom = 10;

var options = {
    projection: new OpenLayers.Projection("EPSG:900913"),
    displayProjection: new OpenLayers.Projection("EPSG:4326"),
    units: "m",
    numZoomLevels: 22,
    maxResolution: 156543.0339,
    maxExtent: new OpenLayers.Bounds(-20037508.34, -20037508.34,
                                     20037508.34, 20037508.34)
};
var map = new OpenLayers.Map('map', options);
if (!googlemaps) {
    var mapnik = new OpenLayers.Layer.TMS(
        "Mappa stradale (OpenStreetMap)",
        "http://tile.openstreetmap.org/",
        {
            type: 'png', getURL: osm_getTileURL,
            displayOutsideMaxExtent: true,
            attribution: '<a href="http://www.openstreetmap.org/">OpenStreetMap</a>'
        }
    );
    map.addLayer(mapnik);
}
if (googlemaps) {
    // create Google Mercator layers
    var gmap = new OpenLayers.Layer.Google(
        "Google",
        {'sphericalMercator': true}
    );
    map.addLayer(gmap);
    var satellite = new OpenLayers.Layer.Google(
        "Satellite (Google)" , {type: G_SATELLITE_MAP, 'sphericalMercator': true}
    );
    map.addLayer(satellite);
    var ibrida = new OpenLayers.Layer.Google(
        "Ibrida (Google)" , {type: G_HYBRID_MAP, 'sphericalMercator': true}
    );
    map.addLayer(ibrida);    
}
map.addControl(new OpenLayers.Control.LayerSwitcher());
mousecontrol = new OpenLayers.Control.MousePosition(),
map.addControl(mousecontrol);
map.setCenter(new OpenLayers.LonLat(lon,lat).transform(map.displayProjection, map.projection), zoom);

function osm_getTileURL(bounds) {
    var res = this.map.getResolution();
    var x = Math.round((bounds.left - this.maxExtent.left) / (res * this.tileSize.w));
    var y = Math.round((this.maxExtent.top - bounds.top) / (res * this.tileSize.h));
    var z = this.map.getZoom();
    var limit = Math.pow(2, z);

    if (y < 0 || y >= limit) {
        return OpenLayers.Util.getImagesLocation() + "404.png";
    } else {
        x = ((x % limit) + limit) % limit;
        return this.url + z + "/" + x + "/" + y + "." + this.type;
    }
}