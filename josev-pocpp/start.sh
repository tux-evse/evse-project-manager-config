#!/usr/bin/env bash
LOG_LEVEL=DEBUG \
    CS_DEFAULT_HEARTBEAT_INTERVAL=30 \
    MQTT_HOST=localhost \
    MQTT_PORT=1883 \
    DATABASE_URL=sqlite:////usr/josev/pocpp/pocpp.db \
    /usr/josev/pocpp/ocpp_service \
    $*
