#!/bin/sh
curl --HEAD -s  $1 | grep location | cut -c 9-23