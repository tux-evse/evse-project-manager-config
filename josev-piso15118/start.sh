#!/usr/bin/env bash
PKIT_PATH=/usr/josev/pki \
MQTT_HOST=localhost \
	MQTT_PORT=1883 \
	LOG_LEVEL=DEBUG \
	/usr/josev/piso15118/iso15118_service \
	$*
