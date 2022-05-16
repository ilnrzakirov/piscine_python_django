#!/bin/zsh

python3 -m venv local_lib
source local_lib/bin/activate
pip3 --version
pip3 install -t local_lib --upgrade git+https://github.com/jaraco/path.py.git > log.log
python3 script.py