#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib64
pkill afb-auth
cynagora-admin set '' 'HELLO' '' '*' yes
clear

# build test config dirname
DIRNAME=`dirname $0`
cd $DIRNAME/..
CONFDIR=`pwd`/etc

echo Auth debug mode config=$CONFDIR/../../etc/*.json

afb-binder --name=afb-energy -v \
  --config=$CONFDIR/binder-test.json \
  --config=$CONFDIR/../../etc/binding-auth.json \
  --config=$CONFDIR/../../etc/binding-scard.json \
  --config=$CONFDIR/../../etc/binding-bia-power.json \
  --config=$CONFDIR/../../etc/binding-debug.json \
  --tracereq=all \
  $*
