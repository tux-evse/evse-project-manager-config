#!/usr/bin/bash
mosquitto_sub -t josev/cs | \
    while read line; do
        is_reset=$(echo $line | jq -r 'select(.name=="reset")')
        if [ -n "$is_reset" ]; then
            echo "REBOOT !!!"
            systemctl reboot
        fi
    done
