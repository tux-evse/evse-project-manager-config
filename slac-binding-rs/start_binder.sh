#!/usr/bin/bash

cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/slac-binding-rs-test/etc/binder-test.json \
                    --config /usr/redpesk/slac-binding-rs-test/etc/binding-slac.json \
                    -v