#!/usr/bin/bash

cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/linky-binding-rs/test/etc/binder-test.json \
                    --config /usr/redpesk/linky-binding-rs/test/etc/binding-linky.json \
                    -v \
                    --tracereq=all \
                    $*