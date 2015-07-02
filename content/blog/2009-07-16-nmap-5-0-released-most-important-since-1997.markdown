---
title: 'Nmap 5.0 Released: Most Important Since 1997!'
author: rami_taibah
layout: post
permalink: /2009/07/nmap-5-0-released-most-important-since-1997/
categories:
- Apps
tags: 
---
\[![trinity-nmapscreen-hd-crop-1200x728](/blog/wp-content/uploads/2009/07/trinity-nmapscreen-hd-crop-1200x728-1024x621.jpg)\]\[1\]
If you don't know what Nmap is then this probably doesn't interest you and/or not "1337" enough. What's wrong with you?
Today, insecure.org announced the release of Nmap 5.0, which they consider the most important release since 1997\. Their [release notes](http://nmap.org/5/) detail the most important changes:
1\. The new \[Ncat \]\[2\] tool aims to be your Swiss Army Knife for data transfer, redirection, and debugging.
2\. The addition of the \[Ndiff scan comparison tool\]\[3\]. Ndiff makes it easy to automatically scan your network daily and report on any changes (systems coming up or going down or changes to the software services they are running).
3\. Nmap performance has \[improved dramatically\]\[4\]. We spent last summer scanning much of the Internet and merging that data with internal enterprise scan logs to determine the most commonly open ports. This allows Nmap to scan fewer ports by default while finding more open ports.
4\. We released \[Nmap Network Scanning\]\[5\], the official Nmap guide to network discovery and security scanning. From explaining port scanning basics for novices to detailing low-level packet crafting methods used by advanced hackers, this book suits all levels of security and networking professionals.
5\. The \[Nmap Scripting Engine (NSE)\]\[6\]: It allows users to write (and share) simple scripts to automate a wide variety of networking tasks. Those scripts are then executed in parallel with the speed and efficiency you expect from Nmap. All existing scripts have been improved, and 32 new ones added.
They also compiled a new Nmap ASCII dragon! How Cool is that?

     (  )   /   _                 (
         |  (   ( .(               )                      _____
           `  `   )              (  ___                 / _   
     (_`    +   . x  ( .            /   ____-----------/ (o)   _
    - .-               +  ;          (  O                           ____
                              )        _____________  `                /
    (__                +- .( -'.- <. - _  VVVVVVV VV V                /
    (_____            ._._: <_ - <- _  (--_AAAAAAA__A_/                |
      .    /./.+-  . .- /  +--  - .     ______________//_              _______
      (__ ' /x  / x _/ (                                  ___'               /
     , x / ( '  . / .  /                                      |              /
        /  /  _/ /    +                                      /              /
       '  (__/                                             /                  
    
                 NMAP IS A POWERFUL TOOL -- USE CAREFULLY AND RESPONSIBLY
    

\[1\]: http://192.168.1.33/blog2/wp-content/uploads/2009/07/trinity-nmapscreen-hd-crop-1200x728.jpg
\[2\]: http://nmap.org/ncat/
\[3\]: http://nmap.org/ndiff/
\[4\]: http://nmap.org/5/\#changes-performance
\[5\]: http://nmap.org/book/
\[6\]: http://nmap.org/book/nse.html