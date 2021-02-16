#!/bin/bash

winid=`xprop -root _NET_ACTIVE_WINDOW | sed 's/^.*# \(0x[^,]*\),.*$/\1/'`
width=$((2 + `xwininfo -stats -id $winid | sed -n 's/^  Width: \([0-9]\+\)$/\1/p'`))
height=$((24 + `xwininfo -stats -id $winid | sed -n 's/^  Height: \([0-9]\+\)$/\1/p'`))
wmctrl -r :ACTIVE: -e 0,$((960 - $width / 2)),$((600 - $height / 2)),-1,-1
