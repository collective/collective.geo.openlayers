DIST_DIR=./src/collective/geo/openlayers/browser/static/openlayers
SOURCE_DIR=./bower_components/openlayers
BOWER_BIN=./node_modules/bower/bin/bower


.PHONY: build dist copysrc

all: dist


build:
	npm install
	$(BOWER_BIN) install
	cd $(SOURCE_DIR)/build/ && python build.py

copysrc:
	cp $(SOURCE_DIR)/build/OpenLayers.js $(DIST_DIR)
	cp -r $(SOURCE_DIR)/img/ $(DIST_DIR)/img
	cp -r $(SOURCE_DIR)/licenses/ $(DIST_DIR)/licenses
	cp -r $(SOURCE_DIR)/theme/ $(DIST_DIR)/theme
	cp -r $(SOURCE_DIR)/lib/OpenLayers/Lang/ $(DIST_DIR)/Lang

dist: build copysrc
