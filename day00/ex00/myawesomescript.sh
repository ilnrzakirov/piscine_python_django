#!/bin/sh
curl --HEAD -s  $1 | grep -i Location | cut -d " " -f 2