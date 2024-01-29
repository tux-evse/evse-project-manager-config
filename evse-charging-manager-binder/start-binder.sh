#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib64
pkill afb-charging
cynagora-admin set '' 'HELLO' '' '*' yes
clear

# build test config dirname
DIRNAME=`dirname $0`
cd $DIRNAME/..
CONFDIR=`pwd`/etc

echo Energy debug mode config=$CONFDIR/../../*.json

afb-binder --name=afb-energy --port=$DEVTOOL_PORT -v \
  --config=$CONFDIR/binder-test.json \
  --config=$CONFDIR/../../etc/binding-i2c.json \
  --config=$CONFDIR/../../etc/binding-am62x.json \
  --config=$CONFDIR/../../etc/binding-chmgr.json \
  --config=$CONFDIR/../../etc/binding-slac.json \
  --config=$CONFDIR/../../etc/binding-debug.json \
  --tracereq=all \
  $*
