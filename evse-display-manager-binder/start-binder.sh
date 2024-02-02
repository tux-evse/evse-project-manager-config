#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib64
pkill afb-display
cynagora-admin set '' 'HELLO' '' '*' yes
clear

# build test config dirname
DIRNAME=`dirname $0`
cd $DIRNAME/..
CONFDIR=`pwd`/etc

echo Display debug mode config=$CONFDIR/*.json

afb-binder --name=afb-display -v \
  --config=$CONFDIR/binder-test.json \
  --config=$CONFDIR/../../etc/binding-display.json \
  --config=$CONFDIR/../../etc/binding-debug.json \
  --binding=/usr/redpesk/display-binding-rs/lib/libafb_display_lvgl.so \
  --tracereq=all \
  $*