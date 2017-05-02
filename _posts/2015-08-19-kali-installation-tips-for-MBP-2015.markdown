---
layout: post
title: Kali installation tips for mac
date: 2015-08-19 
author: Simon
summary: The problems of "unable to boot from USB"
categories: system
tags: 
 - kali
 - Installation
---

# Background 
Kali 2.0 has been released for a while. Most people install Kali on the hard drive through a usb drive. I've seen a lot of people having problems of "black screen after booting from EFI", "got a very small freezing menu in the top left corner" and "Legacy bootloader not found" when trying installing on a Mac. After a few days exploring, I found a solution to the booting issue (and network driver), and now it runs perfectly on my MBP 2015. 

## Problems and Solutions 


### 1. Booting problem
Installation drive boot options screen freezes on Macbook pro 2015 when booting from usb.

Step 1. Prepare 1 USB sticks and a free partition on your hard disk.\\
Step 2. Make a Kali live USB stick following the [**steps**](http://docs.kali.org/downloading/kali-linux-live-usb-install).\\
Step 3. On Mac, open folders EFI - BOOT in your usb drive. Open syslinux.cfg with a text editor.\\
Step 4. Change "vesamenu.c32" to "menu.c32". Save the file.\\
Step 5. Restart the computer, with the option key pressed.\\
Step 6. Choose the EFI option, which is your usb stick.\\
Step 7. Now the boot options should not be freezing any more. Graphical install and install options should work. If this does not work for you, you may stop reading further.

#### 2. Network device not detected
The installation wizard can't identify ethernet card, so just continue without network configured. We will install the network driver later. 


#### 3. Network driver missing
Once you finish installing, boot into Kali, and you will see network device is missing. Type in terminal
{% highlight shell %}
ifconfig
{% endhighlight %}
There is no interface for ethernet or WLAN. 

##### If you are using macbook pro 2015 original wifi adapter
Download the firmware from [**here**](https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/brcm/brcmfmac43602-pcie.bin).  
Copy the file into /lib/firmware/brcm
{% highlight shell %}
root@kali:~# cp /folder/file /lib/firmware/brcm
{% endhighlight %}
Reboot and you will see WiFi is working, but still has no network access.   
Start the network manager by modifying configuration file.
{% highlight shell %}
root@kali:~# nano /etc/NetworkManager/NetworkManager.conf
{% endhighlight %}
Turn false to true, and restart network manager.
{% highlight shell %}
root@kali:~# /etc/init.d/network-manager restart
{% endhighlight %}
Reboot and WiFi should work. This may not work on Thunderbolt-Ethernet wired network.

##### If you are using other network card
{% highlight shell %}
lspci
{% endhighlight %}
lspci is a tool that prints the information about PCI buses and devices in the system. Using this command, find the network controller or ethernet controller model. Try downloading the linux wireless/ethernet firmware that matches the network controller model and put it into the corresponding folder in `/lib/firmware/`


#### 4. Cannot boot into OSX
Step 1. Hold option when booting, and boot from Mac HD.     
Step 2. Reinstall your rEFInd.  
Step 3. Restart.
