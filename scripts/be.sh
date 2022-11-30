#!/bin/sh

set -ex

. .venv/bin/activate

uvicorn \
    be.src.app:app \
    --reload \
    --reload-exclude storage \
    --port 5000
