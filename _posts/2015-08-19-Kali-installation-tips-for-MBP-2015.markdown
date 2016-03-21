---
layout: post
title: Kali installation tips for mac
date: 2015-08-19 
author: yzh503
summary: Summarize all solutions
categories: Linux
tags: 
 - Kali
 - Installation
---

### Background 
Kali 2.0 has been out for a while. Most people install Kali on their hard drive through usb. I've seen lots of people having problems such as "black screen after booting from EFI", "got a very small freezing menu in the top left corner" and "Legacy bootloader not found". After a few days exploring, I found a solution to the booting issue (and network), and now Kali runs perfectly on my MBP 2015. The following are some tricks I did.

### Problems and Solutions 


#### 1. Booting problem

Step 1. Prepare 1 USB sticks and a free partition on your hard disk.     
Step 2. Make a Kali live USB stick. If you are using Mac, follow [**link**](http://docs.kali.org/installation/kali-linux-dual-boot-on-mac-hardware) using dd command (It takes over half an hour). Dual Boot with windows see here [**link**](http://docs.kali.org/installation/dual-boot-kali-with-windows).     
Step 3. Re-plug in the USB stick. In your USB drive, Open folders EFI - BOOT. Open syslinux.cfg with a text editor.     
Step 4. Change "vesamenu.c32" to "menu.c32". Save the file.     
Step 5. Restart the computer, with the option key pressed.     
Step 6. Choose the EFI option, which is your usb stick.        
Step 7. Now the booting menu should not be freezing any more. Graphical install and install options should work. If this does not work for you, you may stop reading further.  


#### 2. Network device not detected

The installation wizard can't identify ethernet card, so just continue without network configured. We will install the network driver later. 


#### 3. Network driver missing

Once you finish installing, boot into Kali, and you will see network device is missing. Type in terminal
{% highlight Bash shell script %}
ifconfig
{% endhighlight %}
There is no interface for ethernet or Wlan. 

##### If you are using macbook pro 2015

download the firmware from [**here**](https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/brcm/brcmfmac43602-pcie.bin).  
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

##### If you are using other network card
{% highlight Bash shell script %}
lspci
{% endhighlight %}
Use this command, find the network controller or ethernet controller model and google it. Try downloading linux wireless/ethernet firmware and put it into the corresponding folder in /lib/firmware/


#### 4. Cannot boot into OSX
Step 1. Hold option when booting, and boot from Mac HD.     
Step 2. Reinstall your rEFInd.  
Step 3. Restart.
