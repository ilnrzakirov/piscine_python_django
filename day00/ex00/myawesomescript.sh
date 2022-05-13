#!/bin/sh
curl --HEAD -s  $1 | grep Location | cut -d " "  -f 2