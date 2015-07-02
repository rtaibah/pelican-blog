---
title: Google Search Straight From the Command Line!
author: rami_taibah
layout: post
permalink: /2008/04/google-search-straight-from-the-command-line/
categories:
- Apps
- Internet
tags: 
---
[![Google Linux](http://192.168.1.33/blog2/wp-content/uploads/2008/04/google-linux.gif)](http://www.tux-planet.fr/blog//)
[Sebastian Bilbeau](http://www.tux-planet.fr/blog//) authored a script that enables you to Google straight from the comfort of your command line interface! How sweet is that? The script will give you the links of the first 11 result in Google, nothing more nothing less. Meaning don't expect it to give you titles and description, very rudimentary stuff I must say, but still it is kinda neat. Cheers Sebi!
You only need to do two simple things, first of all you will need to install the command line browser lynx:
\> sudo apt-get install lynx
You will then need to download a script authored by
\> wget http://public.tux-planet.fr/shell/script-google
Change permissions and rename:
\> chmod +x google.sh && mv google.sh google
Now here is where the fun starts, execution!
\> rami@rami-desktop:~/Desktop$ ./google Royal HeHe2-ness
\> 
\> http://dd0s.jaiku.com/presence/32174627
\> 
\> /blog/ 
\> /blog/linux-general/etymology-of-a-linux-distro/ 
\> /blog/linux-general/the-7-habits-of-highly-effective-linux-u 
\> /blog/linuxhumor/howto-convert-a-friend-to-linux/
Now only if I could figure out the practicality of this? Any ideas guys? ![:)](http://192.168.1.2/blog2/wp-includes/images/smilies/icon_smile.gif)