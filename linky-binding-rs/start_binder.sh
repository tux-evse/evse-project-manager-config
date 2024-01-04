#!/usr/bin/bash

/usr/bin/afb-binder --config /usr/redpesk/linky-binding-rs-test/etc/binder-test.json \
                    --config /usr/redpesk/linky-binding-rs-test/etc/binding-i2c.json \
                    --ws-server sd:i2c \
                    --binding /run/user/$UID/apis/binding/linky-binding-rs