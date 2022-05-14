#!/bin/sh
curl --HEAD -s  $1 | grep location | cut -d " " -f 2