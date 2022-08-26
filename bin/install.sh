#!/usr/bin/env bash
set -x
set -e

TARGET=$1
if [ -d $TARGET ]; then
    cp -r lib code.py $TARGET
fi
