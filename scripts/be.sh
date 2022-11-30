#!/bin/sh

set -ex

. .venv/bin/activate

uvicorn \
    be.api:app \
    --reload \
    --reload-exclude storage \
    --port 5000
