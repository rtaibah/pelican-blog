---
title: 'Howto: Install KDE 4.3 on Ubuntu Jaunty'
author: rami_taibah
layout: post
permalink: /2009/08/howto-install-kde-4-3-on-ubuntu-jaunty/
categories:
- Howto
tags: 
---

![kde430-inspired](http://192.168.1.33/blog2/wp-content/uploads/2009/08/kde430-inspired.png)
KDE 4.3 was released 3 days ago, bringing integration with other technologies, such as PolicyKit, NetworkManager & Geolocation services, was another focus of this release. KRunner's interface has been overhauled. A much more flexible system tray has been developed. Many new Plasmoids have been added, including the openDesktop.org Plasmoid -- an initial take on the Social Desktop. Plasma also receives more keyboard shortcuts.
Unfortunately if you are on Ubuntu Jaunty (or Kubuntu), you will not officially get KDE 4.3\. It will be featured in the upcoming Koala version scheduled in October. However you can get your hands on the latest KDE offering now on your 9.04 desktop. But let us take a quick look at some screenshots.

![kde43-full-thumb-640xauto-7515](http://192.168.1.33/blog2/wp-content/uploads/2009/08/kde43-full-thumb-640xauto-7515.png)

![kde430_thumb](http://192.168.1.33/blog2/wp-content/uploads/2009/08/kde430_thumb.png)

![kde43-social](http://192.168.1.33/blog2/wp-content/uploads/2009/08/kde43-social.png)

## Upgrading to KDE 4.3
First you will need to add the repos to your sources.list file: 
\`sudo sh -c "echo 'deb http://ppa.launchpad.net/kubuntu-ppa/backports/ubuntu jaunty main' \>\> /etc/apt/sources.list"\` 
\`sudo sh -c "echo 'deb http://ppa.launchpad.net/kubuntu-ppa/staging/ubuntu jaunty main' \>\> /etc/apt/sources.list"\`
Add the GPG key: 
\`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8AC93F7A\`
And upgrade: 
\`sudo aptitude update && sudo aptitude dist-upgrade\`
Or if you don't have KDE installed in the first place:
\`sudo aptitude install kubuntu-desktop\`
And they say that the command line is hard! Easy as 1-2-3!
Here is a quick video of KDE 4.3 in action, enjoy!

[](http://192.168.1.33/blog2/wp-content/uploads/2009/08/kde43-social.png)\[youtube kmMdm9liMn4\]

via [Webupd8](http://webupd8.blogspot.com/2009/08/install-kde-43-in-ubuntu-jaunty-904.html), images via [Ars Technica](http://arstechnica.com/open-source/reviews/2009/08/hands-on-kde-43-delivers-a-social-desktop.ars) and [KDE Blog](http://dot.kde.org/2009/08/04/kde-430-released-caizen)