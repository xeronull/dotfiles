#!/usr/bin/env python
#------------------------------
# author: xeronull
# email:  xeronull@protonmail.com
#------------------------------
#
import sys
import webbrowser
import os

print (30 * '-')
print ("\033[1;36m        SEARCH\033[1;m")
print ("\033[1;36m Search for something\033[1;m")
print (30 * '-')
print ("\033[1;36m 1. Search Pornhub\033[1;m")
print ("\033[1;36m 2. Search Idiotbox\033[1;m")
print ("\033[1;36m 3. Search Spankbang\033[1;m")
print ("\033[1;36m 4. Search Pornovideoshub\033[1;m")
print ("\033[1;36m 5. Search Torrentz2\033[1;m")
print ("\033[1;36m 6. Search SoundCloud\033[1;m")
print ("\033[1;36m 7. Search Reddit\033[1;m")
print ("\033[1;36m 8. Search 4chan\033[1;m")
print ("\033[1;36m 9. Search Filesystem\033[1;m")
print ("\033[1;36m10. Search AUR\033[1;m")
print ("\033[1;36m11. Search Wikipedia\033[1;m")
print ("\033[1;36m12. Search Github\033[1;m")
print ("\033[1;36m13. Search Searx\033[1;m")
print (30 * '-')
choice = int(input("Enter your choice [1-10] : "))
if choice == 1:
    browser = webbrowser.get('w3m')
    pornhub = input('What do you want to jerk off to?:')#what do you want it to say?
    browser.open('https://www.pornhub.com/video/search?search=%s' % pornhub)#site you want to search
    print ("Searhing Pornhub...")
elif choice == 2:
    browser = webbrowser.get('w3m')
    idiotbox = input('What do you want to watch?:')
    browser.open('https://codemadness.org/idiotbox/?m=light&q=%s' % idiotbox)
    print ("Searching Idiotbox...")
elif choice == 3:
    browser = webbrowser.get('w3m')
    spankbang = input('What do you want to jerk off to?:')
    browser.open('https://spankbang.com/keyword?keyword=%s' % spankbang)
    print ("Searching Spankbang...")
elif choice == 4:
    browser = webbrowser.get('w3m')
    pornovideoshub = input('What do you want to jerk off to?:')
    browser.open('https://www.pornovideoshub.com/?s=%s' % pornovideoshub)
    print ("Searching Pornovideoshub...")
elif choice == 5:
    browser = webbrowser.get('w3m')
    torrentz = input('What do you want to watch?:')
    browser.open('https://2torrentz.in/search.php?q=%s' % torrentz)
    print ("Searching Torrentz2...")
elif choice == 6:
    browser = webbrowser.get('w3m')
    soundcloud = input('What do you want to listen to?:')
    browser.open('https://www.soundcloud.com/search?btnG=1&q=%s' % soundcloud)
    print ("Searching SoundCloud...")
elif choice == 7:
    browser = webbrowser.get('w3m')
    reddit = input('What do you want to reddit?:')
    browser.open('https://www.reddit.com/search?btnG=1&q=%s' % reddit)
    print ("Searching Reddit...")
elif choice == 8:
    browser = webbrowser.get('w3m')
    fourchan = input('What do you want to 4chan?:')
    browser.open('https://find.4chan.org/?q=%s' % fourchan)
    print ("Searching 4chan...")
elif choice == 9:
    filesystem = input('What do you want to find?:')
    os.system('ranger "%s"' % filesystem)
    print ("Searching filesystem...")
elif choice == 10:
    browser = webbrowser.get('w3m')
    aur = input('What do you want to find?:')
    browser.open('https://aur.archlinux.org/packages/?O=0&K=%s' % aur)
    print ("Searching aur...")
elif choice == 11:
    browser = webbrowser.get('w3m')
    wikipedia = input('What do you want to find?:')
    browser.open('https://en.wikipedia.org/?q=%s' % wikipedia)
    print ("Searching wikipedia...")
elif choice == 12:
    browser = webbrowser.get('w3m')
    github = input('What do you want to find?:')
    browser.open('https://github.com/search?q=%s' % github)
    print ("Searching github...")
elif choice == 13:
    browser = webbrowser.get('w3m')
    searx = input('What do you want to find?:')
    browser.open('https://searx.xyz/?q=%s' % searx)
    print ("Searching searx...")
