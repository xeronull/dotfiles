#!/bin/sh

set -eu

trap 'rm /tmp/places.sqlite' EXIT
cp ~/.mozilla/firefox/crg8cy23.default-release/places.sqlite /tmp

# Select full URL by id if first parameter is a number; can be multiple as 1,2
if echo ${1:-} | grep -q '^[0-9,]\+$'; then
    query="select url from moz_places where id in ($1)"
    sqlite3 -init /dev/null -list /tmp/places.sqlite "$query" 2>&1 | tail -n+2
    exit 0
fi

# Search by url/title, or show everything.
# TODO: allow 'url:x' and 'title:x' to limit search.
query='select
    id,
    strftime("%Y-%m-%d %H:%M", datetime(substr(last_visit_date, 0, 11), "unixepoch")) as last_visit,
    title,
    replace(replace(url, "https://", ""), "http://", "") as url
from moz_places'

[ -n "${1:-}" ] && query="$query where url like '%$1%' or title like '%$1%'"
query="$query order by last_visit_date desc"

w=$(( ($(tput cols) - 28) / 2))
sqlite3 -init /dev/null -column -cmd ".width 7 16 $w $w" /tmp/places.sqlite "$query" 2>&1 | tail -n+2
