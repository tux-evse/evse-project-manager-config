#!/usr/bin/bash
cynagora-admin set '' 'HELLO' '' '*' yes

ln -sf /dev/input/event1 /dev/input/lvgl

echo "Run first: \"export TUX_EVSE_MOCK_PORT=8080;export TUX_EVSE_NATIVE=1; python3 -d  /usr/redpesk/tux-evse-webapp-mock/bin/tux-evse-mock-api.py\""

# build test config dirname
DIRNAME=`dirname $0`
cd $DIRNAME/..
CONFDIR=`pwd`/etc

DEVTOOL_PORT=1235
echo Energy debug mode config=$CONFDIR/*.json port=$DEVTOOL_PORT

/usr/bin/afb-binder --config /usr/redpesk/display-binding-rs/test/etc/binder-test.json \
                    --config /usr/redpesk/display-binding-rs/test/etc/binding-display.json \
                    --ws-client public:unix:@tux-evse-webapp-mock \
                    -v \
                    --tracereq=all \
                    --port=$DEVTOOL_PORT 
                    $*