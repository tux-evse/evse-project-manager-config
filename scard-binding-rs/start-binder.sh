#!/usr/bin/bash

cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/scard-binding-rs/test/etc/binder-test.json \
                    --config /usr/redpesk/scard-binding-rs/test/etc/binding-scard.json \
                    -v