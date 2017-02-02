#!/bin/sh

set -eou

# Install essentials
apk --update add ca-certificates curl python tar py-pip openssl bash zlib-dev snappy-dev lz4-dev yajl-dev

# Install temporary packages
apk add --virtual build-dependencies python-dev build-base wget git

# Install required python packages
pip install --upgrade pip
pip install requests subprocess32 bottle paste cherrypy

#cleanup
apk del build-dependencies
rm -rf /var/cache/apk/*
