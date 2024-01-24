#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib64
pkill afb-display
cynagora-admin set '' 'HELLO' '' '*' yes
clear

# build test config dirname
DIRNAME=`dirname $0`
cd $DIRNAME/..
CONFDIR=`pwd`/etc

DEVTOOL_PORT=1235
echo Display debug mode config=$CONFDIR/*.json port=$DEVTOOL_PORT

afb-binder --name=afb-energy --port=$DEVTOOL_PORT -v \
  --config=$CONFDIR/binder-test.json \
  --config=$CONFDIR/../../etc/binding-display.json \
  --tracereq=all \
  $*