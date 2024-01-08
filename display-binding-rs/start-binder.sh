#!/usr/bin/bash
cynagora-admin set '' 'HELLO' '' '*' yes

ln -sf /dev/input/event1 /dev/input/lvgl

echo "Run first: \"export TUX_EVSE_MOCK_PORT=8080;export TUX_EVSE_NATIVE=1; python3 -d  /usr/redpesk/tux-evse-webapp-mock/bin/tux-evse-mock-api.py\""

/usr/bin/afb-binder --config /usr/redpesk/display-binding-rs/test/etc/binder/test.json \
                    --config /usr/redpesk/display-binding-rs/test/etc/binding-display.json \
                    --ws-client public:unix:@tux-evse-webapp-mock \
                    -v