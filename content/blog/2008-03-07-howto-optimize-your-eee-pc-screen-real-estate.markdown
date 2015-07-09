---
title: 'HOWTO: Optimize Your Eee PC Screen Real Estate'
author: rami_taibah
layout: post
permalink: /2008/03/howto-optimize-your-eee-pc-screen-real-estate/
categories: blog
---
You will probably notice that the default [Ubuntu install](/blog/linuxhowto/howto-install-ubuntu-on-your-eee-pc/ "Ubuntu install") screws up your valuable real estate very badly, everything is just cramped up. We need to do the some tweaks to snug everything into it's place.
\*\*Smaller Fonts:\*\*
`gconftool-2 --set /apps/nautilus/preferences/desktop_font --type string "Sans 8"<br />
gconftool-2 --set /desktop/gnome/interface/document_font_name --type string "Sans 8"<br />
gconftool-2 --set /desktop/gnome/interface/font_name --type string "Sans 8"<br />
gconftool-2 --set /apps/metacity/general/titlebar_font --type string "Sans Bold 8"<br />
gconftool-2 --set /desktop/gnome/interface/monospace_font_name --type string "Monospace 8"<br />
<br style="font-style: italic" />`\* 
Note:Lines might get wrapped, you should paste each line separately in your command line, so just CTRL+- until you get 5 lines\*
\*\*\*All applications can go full-screen using F11\*\*\*
\*\* \*\*
`<em>gconftool-2 --set /apps/metacity/window_keybindings/toggle_fullscreen --type string "F11"</em>`

    

\*\*\*Smaller toolbars using icons only\*\*\*
\*\* \*\*
`<em>gconftool-2 --set /desktop/gnome/interface/toolbar_style --type string "icons"</em>`

    

\*\*\*Setting the right mixer (fixes the mute key)\*\*\*
\*\* \*\*
`<em>gconftool-2 --set /desktop/gnome/sound/default_mixer_tracks --type list --list-type string "[PCM]"</em>`

    

\*\*\*Do not display the incorrect battery warning at login\*\*\*
\*\* \*\*
`<em>gconftool-2 --set /apps/gnome-power-manager/notify/low_capacity --type bool 0</em>`

    

\*\*\*Unconstrain windows to the top of the screen\*\*\*
\*\* \*\*
`<em>gconftool-2 --set /apps/compiz/plugins/move/allscreens/options/constrain_y --type bool 0</em>`

    

\*\*\*Making the top & bottom panels smaller\*\*\*
\*\* \*\*
`<em>gconftool-2 --set /apps/panel/toplevels/top_panel_screen0/size --type integer 19<br />
gconftool-2 --set /apps/panel/toplevels/bottom_panel_screen0/size --type integer 19</em>`

Resolution
You might get 640X480 resolution instead of the 800×480 default resolution. So run the following command: 
`sudo dpkg-reconfigure xserver-xorg`
And choose the defaults on everything, except on the final stage choose 800X480

Minimize the taskbar and autohide it
This one is pretty straight forward. Just right click on both taskbars (top and bottom) and set it to the minimum (19 pixels). You could also autohide the bars, even though I don't like it since a small portion of the taskbars appear when hidden. (Does anybody know how to change that?) 
  

Optimizing Firefox Screen Space
1-To minimize your menu you can install the [tiny menu plugin](https://addons.mozilla.org/en-US/firefox/addon/1455 "tiny menu plugin"), [microfox](https://addons.mozilla.org/en-US/firefox/addon/354 "microfox"), or [littlefox plugin](https://addons.mozilla.org/en-US/firefox/addon/307 "littlefox plugin").
\[![Tiny Menu Plugin For Firefox](http://192.168.1.33/blog2/wp-content/uploads/2008/03/11.png)\]\[1\]\[![Microfox Plugin for Firefox](http://192.168.1.33/blog2/wp-content/uploads/2008/03/2.png)\]\[2\]\[![Littlefox Plugin for Firefox](http://192.168.1.33/blog2/wp-content/uploads/2008/03/1.png)\]\[3\]
[  
](http://192.168.1.33/blog2/wp-content/uploads/2008/03/1.png "Littlefox Plugin for Firefox")[](http://192.168.1.33/blog2/wp-content/uploads/2008/03/1.png "Littlefox Plugin for Firefox")
2-Install the stop-or-reload plugin. This plugin merges the stop and reload button into one.3- Install a compact theme like 
[Whitehart](https://addons.mozilla.org/en-US/firefox/addon/364 "Whitehart").4-Install the [AutohideStatusBar plugin](http://caspar.regis.free.fr/ahs/ "AutohideStatusBar plugin"), to hide the status bar until you are near it.5-Install the [Fullerscreen plugin](https://addons.mozilla.org/en-US/firefox/addon/4650 "Fullerscreen plugin") to get more space when going full screen.
6-Change the overall font size of firefox: 
  
`<br />
cd /home/user/.mozilla/firefox/*.default/chrome/`
Then edit userChrome.css:
\`  
kwrite userChrome.css\`
Then change it to look like this: 
`<br />
* {<br />
font-family: sans-serif !important;<br />
font-size: 8pt !important;<br />
}`
\[1\]: http://192.168.1.33/blog2/wp-content/uploads/2008/03/11.png "Tiny Menu Plugin For Firefox"
\[2\]: http://192.168.1.33/blog2/wp-content/uploads/2008/03/2.png "Microfox Plugin for Firefox"
\[3\]: http://192.168.1.33/blog2/wp-content/uploads/2008/03/1.png "Littlefox Plugin for Firefox"
