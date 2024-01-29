#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib64
pkill afb-energy
cynagora-admin set '' 'HELLO' '' '*' yes
clear

# build test config dirname
DIRNAME=`dirname $0`
cd $DIRNAME/..
CONFDIR=`pwd`/etc

echo Energy debug mode config=$CONFDIR/*.json

afb-binder --name=afb-energy -v \
  --config=$CONFDIR/binder-test.json \
  --config=$CONFDIR/../../etc/binding-energy.json \
  --config=$CONFDIR/../../etc/binding-modbus.json \
  --config=$CONFDIR/../../etc/binding-debug.json \
  --binding=/usr/redpesk/energy-binding-rs/lib/libafb_energy.so \
  --binding=/usr/redpesk/modbus-binding/lib/afb-modbus.so \
  --tracereq=all \
  $*