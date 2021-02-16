#!/bin/bash

winid=`xprop -root _NET_ACTIVE_WINDOW | sed 's/^.*# \(0x[^,]*\),.*$/\1/'`
height=$((24 + `xwininfo -stats -id $winid | sed -n 's/^  Height: \([0-9]\+\)$/\1/p'`))
wmctrl -r :ACTIVE: -e 0,-1,$((1080 - $height)),-1,-1

