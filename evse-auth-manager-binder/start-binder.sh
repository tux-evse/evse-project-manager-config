#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib64
pkill afb-auth
cynagora-admin set '' 'HELLO' '' '*' yes
clear

# build test config dirname
DIRNAME=`dirname $0`
cd $DIRNAME/..
CONFDIR=`pwd`/etc

DEVTOOL_PORT=1235
echo Auth debug mode config=$CONFDIR/../../etc/*.json port=$DEVTOOL_PORT

afb-binder --name=afb-energy --port=$DEVTOOL_PORT -v \
  --config=$CONFDIR/binder-test.json \
  --config=$CONFDIR/../../etc/binding-energy.json \
  --config=$CONFDIR/../../etc/binding-modbus.json \
  --tracereq=all \
  $*