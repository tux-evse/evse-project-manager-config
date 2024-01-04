#!/usr/bin/bash

/usr/bin/afb-binder --config /usr/redpesk/evse-energy-manager-binder-test/etc/binder-test.json \
                    --config /usr/redpesk/evse-energy-manager-binder/etc/binding-energy.json \
                    --config /usr/redpesk/evse-energy-manager-binder/etc/binding-linky.json \
                    --config /usr/redpesk/evse-energy-manager-binder/etc/binding-modbus.json \
                    -v