#!/usr/bin/bash
cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/evse-charging-manager-binder/test/etc/binder-test.json \
                    --config /usr/redpesk/evse-charging-manager-binder/etc/binding-i2c.json \
                    --config /usr/redpesk/evse-charging-manager-binder/etc/binding-ti-am62x.json \
                    -v