#!/bin/bash

# From https://forum.volumio.org/playing-cds-directly-from-mpd-t2411.html

# Count with cdparanoia the tracks
tracks=$(cdparanoia -sQ |& grep -P "^\s+\d+\." | wc -l)

# Add each track to mpd playlist
for ((i=1; i<=$tracks; i++)); do
   mpc add cdda:///$i
done
