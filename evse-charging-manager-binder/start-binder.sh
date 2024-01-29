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
  --binding=/usr/redpesk/i2c-binding-rs/lib/libafb_i2c.so \
  --binding=/usr/redpesk/ti-am62x-binding-rs/lib/libafb_tiam62x.so \
  --binding=/usr/redpesk/charging-binding-rs/lib/libafb_chmgr.so \
  --binding=/usr/redpesk/slac-binding-rs/lib/libafb_slac.so \
  --tracereq=all \
  $*
