#!/bin/sh
rm -rf /tmp/geoserver_testdata
cp -r testdata /tmp/geoserver_testdata
python migrate.py /tmp/geoserver_testdata
