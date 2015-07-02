---
title: 'Compositing With Metacity -- An Early Look'
author: rami_taibah
layout: post
permalink: /2008/10/compositing-with-metacity-another-look/
categories:
- Eye Candy
- Howto
tags: 
---
When the \[compositing capabilities\]\[1\] of Spiftacity \[merged into the Metacity trunk\]\[2\], it caused a fair bit of stir among GNOME users. Included in version 2.21.5 of GNOME, though hidden from casual users, the compositing showed a lot of promise but remained just something to play around with.
The recently released \[GNOME 2.24 \]\[3\]includes the latest builds of \[Metacity\]\[4\], so, unless you've been compiling from tarballs yourself to stay at the bleeding edge, GNOME 2.24 will be the first taste mainstream users will be getting of the latest Metacity developments. While Metacity itself has seen its fair share of tweaking, the compositor, written by \[Iain Holmes\]\[5\] and \[Thomas Thurman\]\[6\], has received a great deal of attention, so perhaps it's time to take a second look at it.
!\[Screenshot\]\[7\]
Metacity's compositor can be enabled in GNOME by launching gconf-editor (alt-F2, type 'gconf-editor' and hit enter), then navigating to apps/metacity/general and setting the key 'compositing\_manager' to true.
\#\#\# Changes
The biggest change I've noted since the compositor's previous incarnation is that the whole thing just feels a lot snappier. On my laptop's Radeon Xpress 200M chip, which is by no means a high-performance card, windows move around just as smoothly as Metacity without compositing, and scrolling in Firefox is smooth and responsive. It performed equally well with both the open source Radeon driver, and the proprietary fgrlx driver.
Smaller developments include tweaking of windows' drop shadows; they are now a bit wider than before, and change depending on whether the window is in focus or not. In previous versions, windows would turn to black squares when they were in the process of minimizing, but they now have reverted back to the classic 'black wireframe' of vanilla Metacity; which is uglier in my opinion, but since it's purely a cosmetic difference as opposed to a functional one, it doesn't really bother me.
\#\#\# Aesthetics
Keeping in line with Metacity's \['boring' \]\[8\]description, the compositor is extremely light on effects; the only things of note are the drop shadows under windows and menus, and the inclusion of window thumbnails when alt-tabbing. The thumbnails aren't updated in real time a la \[Compiz Fusion\]\[9\], but they are an improvement from simple icons.
!\[Screenshot\]\[10\]
One thing to note, is that Metacity's compositing is based on \[Xrender\]\[11\] instead of \[OpenGL\]\[12\], which is lighter on resources and better from a compatibility perspective, but you shouldn't ever expect to be getting cover-switching or getting 'the cube' which \[Compiz\]\[13\] and \[Beryl\]\[14\] became famous for. However, it is lightweight and it may just be what you need if you're after running programs that rely on compositing, such as \[Avant Window Navigator\]\[15\].
My only real complaint is that, much like Metacity itself, the compositor is extremely sparse on configuration options. In fact, outside of forcing some certain changes with Xorg.conf, the compositor only appears to have two options; on and off. The defaults are fine, but there is zero room for tweaking unless you're compiling it yourself. In addition to that, enabling it via gconf-editor is not exactly the most user-friendly way of going about things, though perhaps this is a complaint that is better levelled at the GNOME developers.
\#\#\# The Bottom Line
In its current incarnation, the compositing in Metacity is similar in feel and function to the compositing used in Xfce; it's not particularly attractive looking, but it is extremely stable and performs well on lower-end systems. If you're after features that only compositing can provide but aren't after Compiz' ultra-pretty but ultra-heavy management, you may have tried Metacity's compositing already and been disappointed. However, the new version has dramatically stepped up on stability and performance, so once you've got your hands on GNOME 2.24 you may want to consider giving it another chance.
\[1\]: http://en.wikipedia.org/wiki/Compositing\_window\_manager
\[2\]: http://blog/s.gnome.org/metacity/2007/12/19/compositor-on-trunk/
\[3\]: http://library.gnome.org/misc/release-notes/2.24/
\[4\]: http://en.wikipedia.org/wiki/Metacity
\[5\]: http://blog/s.gnome.org/iain/
\[6\]: http://marnanel.org/writing/about-me
\[7\]: http://www.sandandmercury.net/junk/Screenshot-Configuration%20Editor%20-%20general.jpg
\[8\]: http://en.wikipedia.org/wiki/Metacity\#Philosophy
\[9\]: http://www.compiz-fusion.org/
\[10\]: http://www.sandandmercury.net/junk/Screenshot.jpg
\[11\]: http://en.wikipedia.org/wiki/Xrender
\[12\]: http://en.wikipedia.org/wiki/Opengl
\[13\]: http://en.wikipedia.org/wiki/Compiz
\[14\]: http://en.wikipedia.org/wiki/Beryl\_(window\_manager)
\[15\]: http://en.wikipedia.org/wiki/Avant\_window\_navigator