#!/bin/bash

virtualenv --python=python3 local_lib; source local_lib/bin/activate
pip3 --version
pip3 install -t local_lib --upgrade git+https://github.com/jaraco/path.py.git > my_install.log
python3 script.py