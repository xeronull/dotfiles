#!/bin/bash

winid=`xprop -root _NET_ACTIVE_WINDOW | sed 's/^.*# \(0x[^,]*\),.*$/\1/'`
width=$((2 + `xwininfo -stats -id $winid | sed -n 's/^  Width: \([0-9]\+\)$/\1/p'`))
wmctrl -r :ACTIVE: -e 0,$((1920 - $width)),-1,-1,-1
