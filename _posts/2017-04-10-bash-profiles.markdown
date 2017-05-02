---
layout: post
title: Bash Profiles
date: 2017-04-10
author: Simon
summary: What is the difference between .profile, .bash_profile and .bashrc?
categories: system
tags: 
 - Bash
 - Linux
 - Unix
 - System
---

# Summary Ahead
**~/.bash_profile** **~/.bash_login**,  and  **~/.profile** are read by login shell in that order, but only the first one existing will be loaded by default.

**~/.bashrc** is loaded in non-login shell if it exsits. 

# Background
Bash was developed as a part of GNU project, and now extensively distributed in the POSIX sytems. It uses a collection of startup files to help create an environment. **~/.profile**, **~/.bash_profile** and **~/.bashrc** are the common ones located in the home directory. 

# What are the differences?
**~/.bash_profile**, **~/.bash_login**, **~/.bash_logout** and **~/.bashrc** are specific to the Bash shell, while .profile is a generic config file read by many shells when their specific config files are missing. 

### Login Shell
When bash is a login shell, or invoked with `--login`, it firstly reads and executes commands from the file /etc/profile, if that file exists. Then, it looks for **~/.bash_profile** **~/.bash_login**,  and  .profile, in that order. It **only reads the first one** that is existing and readable. 

### Non-login Shell
When it  is  not a login shell, bash reads and executes commands from /etc/bash.bashrc and **~/.bashrc**, if they exist. 

### Exiting
When a login shell exits, bash reads and executes commands from the file 

### Options
**~/.bash_logout**, if it exists.

The `--noprofile` and `--norc` may be used to start a login and non-login shell without loading profiles.

The `--rcfile` option will force bash to read and execute commands from a user specified file instead of /etc/bash.bashrc and **~/.bashrc**. 

### Load
For convenience, people usually load all other files in .bash_profile and .bashrc. For example, 
{% highlight shell %}
[[ -s "$HOME/.profile" ]] && source "$HOME/.profile" # Load the default .profile 
{% endhighlight %}

# References
Bash man page. 
