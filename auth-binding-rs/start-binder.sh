#!/usr/bin/bash

cynagora-admin set '' 'HELLO' '' '*' yes

/usr/bin/afb-binder --config /usr/redpesk/auth-binding-rs/test/etc/binder-test.json \
                    --config /usr/redpesk/auth-binding-rs/test/etc/binding-auth.json \
                    -v \
                    --tracereq=all \
                    $*