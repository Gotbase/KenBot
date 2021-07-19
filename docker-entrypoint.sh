#!/bin/bash

if [[ -n "${kenbot_CONFIG}" ]]; then
  echo "$kenbot_CONFIG" | tee /kenbot/user/config.json > /dev/null
fi

./kenbot
