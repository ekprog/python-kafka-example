#!/bin/sh
# Docker Entrypoint Script
set -e

if [[ "${1}" = "main.py" ]]; then
  #statements
  echo "${1}"
  exec $(which python3) "${1}"
fi
exec "${@}"