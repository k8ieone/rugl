#!/bin/sh
display_song() {
    status="MPD - Stopped"
    color=
    case $(mpc status | sed 1d | head -n1 | awk '{ print $1 }') in
	'[playing]')
	    status="MPD - Playing"
	    color='#36a8d5'
	    ;;
	'[paused]')
	    status="MPD - Paused"
	    color=
	    ;;
    esac
    echo '[{"name": "mpd", "instance": "now playing", "full_text": "'${status}' '$1'", "color": "'${color}'"}]'
}

(while :; do
	display_song "$(mpc current --wait)"
done) &

while :; do
	display_song "$(mpc current)"
	mpc idle player > /dev/null
done