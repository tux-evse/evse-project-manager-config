#!/usr/bin/bash
cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/evse-display-manager-binder/test/etc/binder-test.json \
                    --config /usr/redpesk/evse-display-manager-binder/etc/binding-display.json \
                    -v \
                    --tracereq=all \
                    $*