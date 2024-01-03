#!/usr/bin/bash

/usr/bin/afb-binder --config /usr/redpesk/evse-charging-manager-binder/etc/binder-test.json \
                    --config /usr/redpesk/evse-charging-manager-binder/etc/binding-i2c.json \
                    --config /usr/redpesk/evse-charging-manager-binder/etc/binding-ti-am62x.json \
                    --ws-server sd:chg-mgr \
                    --binding /run/$UID/api/binding/i2c-binding-rs \
                    --binding /run/$UID/api/binding/ti-am62x-binding-rs