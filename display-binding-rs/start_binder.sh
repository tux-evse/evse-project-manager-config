#!/usr/bin/bash

ln -sf /dev/input/event1 /dev/input/lvgl

/usr/bin/afb-binder --config /usr/redpesk/display-binding-rs-test/etc/binder-test.json \
                    --config /usr/redpesk/display-binding-rs-test/etc/binding-display.json \
                    -v