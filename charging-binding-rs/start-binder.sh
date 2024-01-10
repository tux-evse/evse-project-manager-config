#!/usr/bin/bash

cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/charging-binding-rs/test/etc/binder-test.json \
                    --config /usr/redpesk/charging-binding-rs/test/etc/binding-charging.json \
                    -v