#!/usr/bin/bash
jq '.set."libafb_josev.so".cs_parameters' /usr/redpesk/evse-charging-manager-binder/etc/binding-josev-ac.json > /tmp/cs_config.json
jq '.set."libafb_josev.so".cs_status_and_limits' /usr/redpesk/evse-charging-manager-binder/etc/binding-josev-ac.json > /tmp/cs_limits.json
CS_CONFIG_FILE=/tmp/cs_config.json CS_LIMITS_FILE=/tmp/cs_limits.json LOG_LEVEL=DEBUG /usr/josev/rslac/slac_service
