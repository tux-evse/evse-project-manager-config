#!/usr/bin/bash
cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/modbus-binding-test/etc/binder-test.json \
                    --config /usr/redpesk/modbus-binding-test/etc/binding-modbus.json \
                    -v
                    