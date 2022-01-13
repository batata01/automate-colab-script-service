#!/bin/bash

MOZ_HEADLESS=1 /usr/bin/python /root/work/colabscript/script.py
bash /root/work/colabscript/move.sh
killall -q -9 firefox
