#!/usr/bin/bash
cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/energy-binding-rs/test/etc/binder-test.json \
                    --config /usr/redpesk/energy-binding-rs/test/etc/binding-energy.json \
                    --config /usr/redpesk/energy-binding-rs/test/etc/binding-linky.json \
                    --config /usr/redpesk/energy-binding-rs/test/etc/binding-modbus.json \
                    -v