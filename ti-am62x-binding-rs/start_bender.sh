#!/usr/bin/bash

/usr/bin/afb-binder --config /usr/redpesk/ti-am62x-binding-rs-test/etc/binder-test.json \
                    --config /usr/redpesk/ti-am62x-binding-rs-test/etc/binding-ti-am62x.json \
                    --config /usr/redpesk/ti-am62x-binding-rs-test/etc/binding-i2c.json \
                    --ws-server sd:ti-am62x \
                    --binding /run/$UID/api/binding/ti-am62x-binding-rs
                    