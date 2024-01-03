#!/usr/bin/bash

/usr/bin/afb-binder --config /usr/redpesk/i2c-binding-rs-test/etc/binder-test.json \
                    --config /usr/redpesk/i2c-binding-rs-test/etc/binding-i2c.json \
                    --ws-server sd:i2c \
                    --binding /run/user/$UID/apis/binding/i2c-binding-rs