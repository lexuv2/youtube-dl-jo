#!/bin/bash

set -e

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip uninstall -y youtube-dl

deactivate

set +e
rm -rf venv