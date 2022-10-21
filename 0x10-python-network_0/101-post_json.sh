#!/bin/bash
# posts a json file
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
