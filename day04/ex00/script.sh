#!/bin/zsh

python3 -m venv django_venv
source django_venv/bin/activate
django_venv/bin/pip3 install --force-reinstall -r requirement.txt
django-admin startproject d04
cd d04
django-admin startapp ex00
