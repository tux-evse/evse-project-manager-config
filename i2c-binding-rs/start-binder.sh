#!/usr/bin/bash

cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/i2c-binding-rs/test/etc/binder-test.json \
                    --config /usr/redpesk/i2c-binding-rs/test/etc/binding-i2c.json \
                    -v \
                    --tracereq=all \
                    $*