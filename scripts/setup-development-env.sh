#!/usr/bin/env bash
set -e

rm -rf .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
