---
title: 'HOWTO: Install Ubuntu on Your Eee PC'
author: rami_taibah
layout: post
permalink: /2008/02/howto-install-ubuntu-on-your-eee-pc/
categories: blog
---
I have [posted](/blog/linux-general/eee-pcfinally/) earlier that the "easy mode" of the Eee PC is like living on the bottom bunker in a basement cell of the Alcatraz. Liberating it to the default Xandros "advanced mode" is just like going out to yard with sweaty inmates, which isn't saying much.
I initially installed eeexubuntu on that little critter, but soon was disenchanted. XFCE is just not for me. Solution? Install everybody's favorite! Ubuntu!
\#\# USB disk or CD drive?
Installing a different distro on your Eee PC is done either by using a USB thumb drive or an external CD drive. I expect that the Eee PC is the first Linux experience to a lot of Eee PC users, so I would recommend getting an external CD drive, it's much less of a hassle.
\#\# Downloading, burning, and preperation
First of all you will need to get Ubuntu. At the time of writing this, Ubuntu 7.10 (Gutsy) is the latest so get it either through direct [download](http://www.ubuntu.com/getubuntu/download) or \[torrent\]\[1\].
Then you will need to burn it on a CD using your favorite image burner. (there are many guides for that, google it)
You will also probably need to edit the boot sequence in your bios. So restart your Eee PC and press F2 to enter the bios menu and change the primary boot to "USB Optical Drive". Pop in the Ubuntu CD in your external drive and restart. Then press enter when you get the list of options (first option).
A couple of minutes later you will be on your default Ubuntu desktop. Before clicking the "install" icon, you will need to disable the desktop effects. Since the installer doesn't fit into the small Eee PC screen, you will need to use the ALT+Right click option to move the installer window. So System --\> Prefrences --\> Appearence and then go to the last tab "Visual Effects" and then select none.
\#\# Installation
Now you are ready for installing, so click on the "Install" icon located on your desktop (pictures are eclipsed due to screen size):
\[![Eee PC Ubuntu Install](http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot1.png)\]\[2\]
Select your language.
\[![Eee PC Ubuntu Install](http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-2.png)\]\[3\]
Select your keyboard layout.
\[![Eee PC Ubuntu Install](http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-3.png)\]\[4\]
Select manual partitioning.
\[![Eee PC Ubuntu Install](http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-4.png)\]\[5\]
This is the tricky part, basically you will need to set a root partition for the system to be installed in. So we are going to partition /dev/sda1 and make it our root. Click on /dev/sda1 and then delete whatever partitions under it. Then click on new and in filesystem choose ext2 (we are not going to use ext3 because we want to limit writes due to the solid state disk nature of the Eee PC). Also set mount point to "/" (without the quotes).
If you have an SDHC card click on it and edit the mount point to "/media/\*whatever\*". If you have nothing interesting in that card you might want to just delete whatever partitions and make a new partition, and choosing the filesystem as "fat32″. Since you never know when you might want to use it on Windows machine ;).
\[![Eee PC Ubuntu Install](http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-5.png)\]\[6\]
Enter your details. Name, user name, password, and machine name. Click next.
You will be prompted with a warning that all your data will be wiped out, click OK. Now sit back and relax, your system will be ready in 30 minutes or so.
Thats it! Now just click restart system when prompted, you will then asked to eject CD.
Now your golden ![:)](http://192.168.1.2/blog2/wp-includes/images/smilies/icon_smile.gif)
A lot of functionality will be missing with this out of the box Ubuntu installation. For example your wireless won't function. Visit my \[Perfect Eee PC Ubuntu Installation Guide\]\[7\] for a complete guide on how to get things up and running.
\[1\]: http://torrent.ubuntu.com:6969/file?info\_hash=%ED%8A%B7%FB%3AL%D3Nd%8EH%A4%0F%8F%DD%97%A4%F5%40%D2
\[2\]: http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot1.png "Eee PC Ubuntu Install"
\[3\]: http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-2.png "Eee PC Ubuntu Install"
\[4\]: http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-3.png "Eee PC Ubuntu Install"
\[5\]: http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-4.png "Eee PC Ubuntu Install"
\[6\]: http://192.168.1.33/blog2/wp-content/uploads/2008/02/screenshot-5.png "Eee PC Ubuntu Install"
\[7\]: /blog/linuxhowto/howto-your-perfect-ubuntu-on-your-perfect-eee-pc/