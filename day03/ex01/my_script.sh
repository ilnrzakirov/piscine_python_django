#!/bin/zsh

python3 -m venv local_lib
source local_lib/bin/activate
pip3 --version
pip3 install --log log.log -t local_lib --upgrade --force-reinstall git+https://github.com/jaraco/path.py.git
python3 my_program.py