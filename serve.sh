#!/bin/bash
python3 -m venv ~/virtual-envs/mkdocs
source ~/virtual-envs/mkdocs/bin/activate
pip install -r requirements.txt
#mkdocs build
pip list | grep mkdocs
read -p "Press enter to continue"
mkdocs serve
deactivate
