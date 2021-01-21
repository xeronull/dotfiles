 #!/bin/bash

 # Extracts today's Firefox link history and leverages Rofi
 # to present them to the user.

 # Find all profiles' places.sqlite files.
 dbPaths=$(find ~/.mozilla/firefox/ -type f -name "places.sqlite" -mindepth 2 -maxdepth 2 2>/dev/null)

 for dbPath in $dbPaths;
 do
	     # Firefox's bookmarks db is locked when in use so copy it first to a temporary file.
	         tempFile="firefox_history-$RANDOM.tmp"
		     cp $dbPath ~/$tempFile
		         dbPath=~/$tempFile

			     # Ask Firefox nicely for the today's history.
			         query="select p.url from moz_historyvisits as h, moz_places as p where substr(h.visit_date, 0, 11) >= strftime('%s', date('now')) and p.id == h.place_id order by h.visit_date;"
				     todaysLinks=$(sqlite3 "$dbPath" "$query")
				         echo "$todaysLinks" > ~/Documents/todays_links.txt

					     # Cleanup in isle 4.
					         rm ~/$tempFile
					 done

					 # Remove duplicate entries and throw it to Rofi for output.
					 openHistory=$(awk '!a[$0]++' ~/Documents/todays_links.txt | rofi -dmenu -p "Link History: " -i -lines 45 -width 50 -hide-scrollbar -separator-style none -show-icons true -drun-icon-theme "Mint-X-Purple")

					 # Do not run if user pressed ESC.
					 if [ $openHistory ]; then
						     xdg-open $openHistory
					 fi

