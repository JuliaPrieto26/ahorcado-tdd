#!/bin/sh
if command -v nodejs >/dev/null 2>&1 ; then
    echo "nodejs found"
    echo "version: $(nodejs -v)"
else
    echo "nodejs not found"
fi
