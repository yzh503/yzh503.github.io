---
layout: post
title: Kali installation tips for Macbook Pro 2015
date: 2015-08-19 
author: yzh503
summary: Summarize all solutions
categories: Linux
tags: 
 - Kali
 - Macbook
 - Installation
---

###Background 
Kali 2.0 live USB doesn't' really well support Macbook pro 2015 Retina. I've seen lots of people having problems like "black screen after booting from EFI", "got a very small freezing menu in the top left corner", and "Legacy bootloader not found". After a few days exploring, I suddenly found a solution to the booting issue (and network), and now Kali 2.0 runs perfectly on my MBP 2015. The following are some tricks I did.

###Problems and Solutions 


####1. Booting problem

Step 1. Prepare 2 USB sticks and a free partition.  
Step 2. Make a Ubuntu USB drive (simply extract ".iso" file into USB drive).    
Step 3. Make a Kali live USB stick following [**link**](http://docs.kali.org/downloading/kal...ve-usb-install) using dd command (It takes over half an hour).   
Step 4. Plug in **BOTH** USB sticks, and restart the computer, with the option key pressed.     
Step 5. Choose one of the EFI options. If you are not sure, just randomly try one. In my experience, The first EFI option is usually from the left USB port.        
Step 6. Now the booting menu is not freezing! If this does not work for you, you may stop reading further.  
Step 7. Play with Kali live for a while if you want. To install Kali on hard disk, go back to boot up menu, and select graphic install. Live installation failed to install grub on my computer for some reason.


####2. Network device not detected

The installation wizard can't identify ethernet card, so just continue without network configured. We will install the network driver later.


####3. Network driver 

Once you finish installing, boot into Kali, and you will see network device is missing. Type in terminal
{% highlight Bash shell script %}
ifconfig
{% endhighlight %}
There is only localhost "lo". To fix this, download the firmware for macbook pro 2015 from [**here**](https://git.kernel.org/cgit/linux/ke...43602-pcie.bin).       
Copy the file into /lib/firmware/brcm
{% highlight Bash shell script %}
root@kali:~# cp /folder/file /lib/firmware/brcm
{% endhighlight %}
Reboot and you will see WiFi is working, but still has no network access.   
Start the network manager by modifying configuration file.
{% highlight Bash shell script %}
root@kali:~# nano /etc/NetworkManager/NetworkManager.conf
{% endhighlight %}
Turn false to true, and restart network manager.
{% highlight Bash shell script %}
root@kali:~# /etc/init.d/network-manager restart
{% endhighlight %}
Reboot and WiFi should work. This may not work on Thunderbolt-Ethernet wired network.

####4. Cannot boot into OSX
Step 1. Hold option when booting, and boot from Mac HD.     
Step 2. Reinstall your rEFInd.  
Step 3. Restart.


###Summary
Note that the booting problem is only reported with Macbook pro 2015 this specific model. The reason why Kali boot loader freezes on MBP 2015 is unknown. There is no enough detailed information about early boot process and Kali boot loader. I'm not sure if anything is missing in Kali, or MBP 2015 got something new that conflicts with Kali boot loader, or it's some other mysterious problems. The only thing that we know is that Kali boot loader could not be properly loaded without another bootable linux USB drive plugged in. I'll write another post to analyse.