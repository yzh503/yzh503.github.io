---
layout: post
title: Bash Commands
date: 2017-05-02
author: Simon
summary: Get familiar with command line interface
categories: cli
tags: 
 - bash
 - linux
 - unix
 - system
 - shell
---

# How do commands work?
In Unix/Linux systems, commands in a Unix shell are all programs. Anything you enter into the shell is called standard input. Similarly, Anything printed on the shell is standard output. programs are binary files, which contains computer readable code. By default, all commands/programs invoked from the shell are located somewhere in the system. Not all programs in the system can be directly called in the shell. For example,
{% highlight shell %}
$ echo "echo is a program located in /bin"
echo is a program located in /bin/echo
{% endhighlight %}
`echo` is a common command in Linux/Unix. It is in fact a program located in the directory `/bin`. Let's see where it is located. 
{% highlight shell %}
$ whereis echo
echo: /bin/echo /usr/share/man/man1/echo.1.gz
{% endhighlight %}
How does the shell know where it is located? 
The most direct way of executing a program in the shell is to enter the absolute/relative path of the prgram followed by parameter. For example,
{% highlight shell %}
$ /bin/echo "This is a parameter"
This is a parameter
{% endhighlight %}
`/bin/echo` is the path echo, and the string is a parameter. The Environment variable $PATH tells the shell where all the commands are from. Internally, the shell looks for the program in the directories listed in $PATH ($var indicates variable in the Bash shell). If you want to make a program into a command and run it without entering its path, you will need to manually add the path into $PATH. For one-time use, run the command to add /opt/bin/ into $PATH, 
{% highlight shell %}
$ PATH=$PATH:~/opt/bin
{% endhighlight %}
Or, if you want to make the variable available to other programs, 
{% highlight shell %}
$ export PATH=$PATH:~/opt/bin
{% endhighlight %}
Add the command into your bash profile such as `~/.bash_profile`, so that it will be executed everytime a bash instance is open. 

# Some Useful Bash Commands
### Manual
`man` is the most useful command ever. It prints the manual page of system tools. For example, 
{% highlight shell %}
$ man du
{% endhighlight %}
This gives you the full manual of the program "disk usage".
### Redirect std I/O
Redirect standard output to a file. Overwrite the given file if it already exists.
{% highlight shell %}
$ program > filename # redirect output to a file
$ program >> filename # append
{% endhighlight %}
`#` is comments.

Redirect input from a file. This can be used to input complex parameters, or automated execution. This will give an error if the file doesn’t exist. 
{% highlight shell %}
$ program < filename # redirect input from a file
{% endhighlight %}

Redirect stderr to a file. This will overwrite the given file if it already exists. 
{% highlight shell %}
$ program 2> filename  # redirect error to a file
$ program 2>> filename #append
{% endhighlight %}

If you want clean output, redirect some outputs to the black hole. 
{% highlight shell %}
$ program 2> /dev/null  # not printing error
$ program > /dev/null   # not printing anything
{% endhighlight %}

### Pipe
Pipes `|` use the output of a program as the input of another program
{% highlight shell %}
$ program1 | program2 
$ ls | grep "file" # searching file
$ cat file.output | grep "text" # searching text
{% endhighlight %}


### Standard Wildcard

| Char  | Meaning |
|:--------|:-------:|
| *   | any number of characters   |
| ?   | any single character  |
|----
| [ab]   | a or b   |
| [a-c]   | a to c   |
|=====
| {foo, bar}   | String foo or bar   |
{: rules="groups"}

Bash also support regular expression, which is powerful for pattern matching. 

# Remove
rm is a dangerous command. [**rmtrash**](https://github.com/PhrozenByte/rmtrash) is an alternative to rm that puts files using trush-put. 

# Run a program without getting out of the shell
{% highlight shell %}
$ program &
{% endhighlight %}
Use process control commands to manage them, such as `ps`, `jobs`, `fg`, `bg`, `kill`.
# Reference
Below tables are derived from [here](http://courses.cs.washington.edu/courses/cse390a/14au/bash.html).
<table id="commands" class="standard" >
  <tbody><tr>
    <th>Category</th>
    <th width="20%">Command</th>
    <th>Description</th>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="4">basic shell</th>
    <td><a href="http://linux.die.net/man/1/clear" title="click to see detailed documentation about the clear command"><code class="unixcommand">clear</code></a></td>
    <td>clear all previous commands' output text from the terminal</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/exit" title="click to see detailed documentation about the exit command"><code class="unixcommand builtin">exit</code></a> (or <a href="http://linux.die.net/man/1/logout" title="click to see detailed documentation about the logout command"><code class="unixcommand builtin">logout</code></a>)</td>
    <td>quits the shell</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/alias" title="click to see detailed documentation about the alias command"><code class="unixcommand builtin">alias</code></a>, <a href="http://linux.die.net/man/1/unalias" title="click to see detailed documentation about the unalias command"><code class="unixcommand builtin">unalias</code></a></td>
    <td>give a pseudonym to another command <br>
      (you may need to enclose the command in quotes if it contains spaces or operators)
    </td>
  </tr><tr>
    <td><a href="http://linux.die.net/man/1/history" title="click to see detailed documentation about the history command"><code class="unixcommand builtin">history</code></a></td>
    <td>show a list of all past commands you have typed into this shell</td>
  </tr>
  
  
  <tr class="firstrow">
    <th rowspan="5">directories</th>
    <td><a href="http://linux.die.net/man/1/ls" title="click to see detailed documentation about the ls command"><code class="unixcommand">ls</code></a></td>
    <td>list files in a directory</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/pwd" title="click to see detailed documentation about the pwd command"><code class="unixcommand builtin">pwd</code></a></td>
    <td>displays the shell's current working directory</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/cd" title="click to see detailed documentation about the cd command"><code class="unixcommand builtin">cd</code></a></td>
    <td>changes the shell's working directory to the given directory; can be a relative or absolute path</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/mkdir" title="click to see detailed documentation about the mkdir command"><code class="unixcommand">mkdir</code></a></td>
    <td>creates a new directory with the given name</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/rmdir" title="click to see detailed documentation about the rmdir command"><code class="unixcommand">rmdir</code></a></td>
    <td>removes the directory with the given name (the directory must be empty)</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="4">file operations</th>
    <td><a href="http://linux.die.net/man/1/cp" title="click to see detailed documentation about the cp command"><code class="unixcommand">cp</code></a></td>
    <td>copies a file/directory</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/mv" title="click to see detailed documentation about the mv command"><code class="unixcommand">mv</code></a></td>
    <td>moves (or renames) a file/directory</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/rm" title="click to see detailed documentation about the rm command"><code class="unixcommand">rm</code></a></td>
    <td>deletes a file</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/touch" title="click to see detailed documentation about the touch command"><code class="unixcommand">touch</code></a></td>
    <td>update the last-modified time of a file (or create an empty file)</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="6">file examination</th>
    <td><a href="http://linux.die.net/man/1/cat" title="click to see detailed documentation about the cat command"><code class="unixcommand">cat</code></a></td>
    <td>output the contents of a file</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/more" title="click to see detailed documentation about the more command"><code class="unixcommand">more</code></a> (or <a href="http://linux.die.net/man/1/less" title="click to see detailed documentation about the less command"><code class="unixcommand">less</code></a>)</td>
    <td>output the contents of a file, one page at a time</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/head" title="click to see detailed documentation about the head command"><code class="unixcommand">head</code></a>, <a href="http://linux.die.net/man/1/tail" title="click to see detailed documentation about the tail command"><code class="unixcommand">tail</code></a></td>
    <td>output the beginning or ending of a file</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/wc" title="click to see detailed documentation about the wc command"><code class="unixcommand">wc</code></a></td>
    <td>output a count of the number of characters, lines, words, etc. in a file</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/du" title="click to see detailed documentation about the du command"><code class="unixcommand">du</code></a></td>
    <td>report disk space used by a file/directory. Personally I use <code>du -sh *</code> the most to check disk usage.</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/diff" title="click to see detailed documentation about the diff command"><code class="unixcommand">diff</code></a></td>
    <td>output differences between two files</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="4">file permissions</th>
    <td><a href="http://linux.die.net/man/1/chmod" title="click to see detailed documentation about the chmod command"><code class="unixcommand">chmod</code></a></td>
    <td>change the permissions on a file or group of files</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/chown" title="click to see detailed documentation about the chown command"><code class="unixcommand">chown</code></a></td>
    <td>change the owner of a file</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/chgrp" title="click to see detailed documentation about the chgrp command"><code class="unixcommand">chgrp</code></a></td>
    <td>change the group associated with a file</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/umask" title="click to see detailed documentation about the umask command"><code class="unixcommand">umask</code></a></td>
    <td>change the default permissions given to newly created files</td>
  </tr>

  <tr class="firstrow">
    <th rowspan="7">searching and sorting</th>
    <td><a href="http://linux.die.net/man/1/grep" title="click to see detailed documentation about the grep command"><code class="unixcommand">grep</code></a></td>
    <td>search a file for a given string or expression</td>
  </tr>

  <tr>
    <td><a href="http://linux.die.net/man/1/sort" title="click to see detailed documentation about the sort command"><code class="unixcommand">sort</code></a></td>
    <td>convert an input into a sorted output</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/uniq" title="click to see detailed documentation about the uniq command"><code class="unixcommand">uniq</code></a></td>
    <td>strip duplicate lines</td>
  </tr>

  <tr>
    <td><a href="http://linux.die.net/man/1/find" title="click to see detailed documentation about the find command"><code class="unixcommand">find</code></a></td>
    <td>search for files by name within a given directory</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/xargs" title="click to see detailed documentation about the xargs command"><code class="unixcommand">xargs</code></a></td>
    <td>
      launch a command over each of a set of lines of input (often used with <code>find</code>)
    </td>
  </tr>

  <tr>
    <td><a href="http://linux.die.net/man/1/locate" title="click to see detailed documentation about the locate command"><code class="unixcommand">locate</code></a></td>
    <td>search for files by name on the entire system</td>
  </tr>

  <tr>
    <td><a href="http://linux.die.net/man/1/which" title="click to see detailed documentation about the which command"><code class="unixcommand">which</code></a></td>
    <td>shows the complete path of a command or file</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="4">compression</th>
    <td><a href="http://linux.die.net/man/1/zip" title="click to see detailed documentation about the zip command"><code class="unixcommand">zip</code></a>, <a href="http://linux.die.net/man/1/unzip" title="click to see detailed documentation about the unzip command"><code class="unixcommand">unzip</code></a></td>
    <td>create a .zip archive or extract its contents</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/tar" title="click to see detailed documentation about the tar command"><code class="unixcommand">tar</code></a></td>
    <td>Unix archiving/de-archiving program</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/gzip" title="click to see detailed documentation about the gzip command"><code class="unixcommand">gzip</code></a>, <a href="http://linux.die.net/man/1/gunzip" title="click to see detailed documentation about the gunzip command"><code class="unixcommand">gunzip</code></a></td>
    <td>GNU compression/decompression programs</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/bzip2" title="click to see detailed documentation about the bzip2 command"><code class="unixcommand">bzip2</code></a>, <a href="http://linux.die.net/man/1/bunzip2" title="click to see detailed documentation about the bunzip2 command"><code class="unixcommand">bunzip2</code></a></td>
    <td>improved compression/decompression programs</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="4">system information</th>
    <td><a href="http://linux.die.net/man/1/date" title="click to see detailed documentation about the date command"><code class="unixcommand">date</code></a></td>
    <td>outputs the current date/time</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/cal" title="click to see detailed documentation about the cal command"><code class="unixcommand">cal</code></a></td>
    <td>outputs an ASCII calendar</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/uname" title="click to see detailed documentation about the uname command"><code class="unixcommand">uname</code></a></td>
    <td>print information about the system</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/time" title="click to see detailed documentation about the time command"><code class="unixcommand">time</code></a></td>
    <td>measure how long a program takes to run</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="8">process management</th>
    <td><a href="http://linux.die.net/man/1/ps" title="click to see detailed documentation about the ps command"><code class="unixcommand">ps</code></a>, <a href="http://linux.die.net/man/1/jobs" title="click to see detailed documentation about the jobs command"><code class="unixcommand builtin">jobs</code></a></td>
    <td>list the processes you are running;
      every process has a unique integer id number (PID)
    </td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/top" title="click to see detailed documentation about the top command"><code class="unixcommand">top</code></a></td>
    <td>see what processes are using the most CPU/memory, and show system memory/CPU stats</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/kill" title="click to see detailed documentation about the kill command"><code class="unixcommand">kill</code></a></td>
    <td>terminate a process</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/killall" title="click to see detailed documentation about the killall command"><code class="unixcommand">killall</code></a></td>
    <td>terminate a group of processes by name</td>
  </tr>
  <tr>
    <td><code>^C</code> or <code>^\</code></td>
    <td>(hotkey) terminates (kills) the currently running process</td>
  </tr>
  <tr>
    <td><code>^Z</code></td>
    <td>(hotkey) suspends the currently running process</td>
  </tr>
  <tr>
    <td><code>&amp;</code></td>
    <td>(special character) when <code>&amp;</code> is placed at the end of a command, that command is run in the background (shell does not wait for the command to finish before returning to the input prompt)</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/bg" title="click to see detailed documentation about the bg command"><code class="unixcommand builtin">bg</code></a>, <a href="http://linux.die.net/man/1/fg" title="click to see detailed documentation about the fg command"><code class="unixcommand builtin">fg</code></a></td>
    <td>starts a suspended process running in the background or foreground</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="5">users and groups</th>
    <td><a href="http://linux.die.net/man/1/whoami" title="click to see detailed documentation about the whoami command"><code class="unixcommand">whoami</code></a></td>
    <td>outputs your user name</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/passwd" title="click to see detailed documentation about the passwd command"><code class="unixcommand">passwd</code></a></td>
    <td>changes your password</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/groups" title="click to see detailed documentation about the groups command"><code class="unixcommand">groups</code></a></td>
    <td>list the groups to which a user belongs</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/sudo" title="click to see detailed documentation about the sudo command"><code class="unixcommand">sudo</code></a></td>
    <td>execute a single command as the super-user</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/su" title="click to see detailed documentation about the su command"><code class="unixcommand">su</code></a></td>
    <td>log in to a shell as the super-user</td>
  </tr>

  <!--
  <tr>
    <td><code class="unixcommand">chroot</code></td>
    <td>run a command with a modified root directory (to prevent it from doing bad things)</td>
  </tr>
  -->
  
  <tr class="firstrow">
    <th rowspan="5">multi-user environments</th>
    <td><a href="http://linux.die.net/man/1/hostname" title="click to see detailed documentation about the hostname command"><code class="unixcommand">hostname</code></a></td>
    <td>outputs the name of the current computer/server</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/w" title="click to see detailed documentation about the w command"><code class="unixcommand">w</code></a>, <a href="http://linux.die.net/man/1/finger" title="click to see detailed documentation about the finger command"><code class="unixcommand">finger</code></a></td>
    <td>see who is logged in to this computer</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/write" title="click to see detailed documentation about the write command"><code class="unixcommand">write</code></a></td>
    <td>sends a message to another user logged in to this computer</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/wall" title="click to see detailed documentation about the wall command"><code class="unixcommand">wall</code></a></td>
    <td>broadcasts a message to all other users logged in to this computer</td>
  </tr>
  <tr>
    <td><code>.plan</code></td>
    <td>(filename) a special hidden file you can create in your home directory, whose contents will be displayed when other users run <code>finger</code> on you.  Was originally intended to be used to tell others what you are up to right now.  (the Twitter of the 1970s!)</td>
  </tr>

  <tr class="firstrow">
    <th rowspan="5">network</th>
    <td><a href="http://linux.die.net/man/1/links" title="click to see detailed documentation about the links command"><code class="unixcommand">links</code></a>, <a href="http://linux.die.net/man/1/lynx" title="click to see detailed documentation about the lynx command"><code class="unixcommand">lynx</code></a></td>
    <td>text-only web browsers (yes, really)</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/ssh" title="click to see detailed documentation about the ssh command"><code class="unixcommand">ssh</code></a>, <a href="http://linux.die.net/man/1/sftp" title="click to see detailed documentation about the sftp command"><code class="unixcommand">sftp</code></a>, <a href="http://linux.die.net/man/1/scp" title="click to see detailed documentation about the scp command"><code class="unixcommand">scp</code></a></td>
    <td>connect to a remote Unix server; open a shell on it or send/receive files from it</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/wget" title="click to see detailed documentation about the wget command"><code class="unixcommand">wget</code></a></td>
    <td>download from a URL and save it to a file on the local hard drive</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/curl" title="click to see detailed documentation about the curl command"><code class="unixcommand">curl</code></a></td>
    <td>download from a URL and output its contents to the console</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/pine" title="click to see detailed documentation about the pine command"><code class="unixcommand">pine</code></a>, <a href="http://linux.die.net/man/1/mail" title="click to see detailed documentation about the mail command"><code class="unixcommand">mail</code></a></td>
    <td>text-only email programs</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="3">text editors</th>
    <td><a href="http://linux.die.net/man/1/pico" title="click to see detailed documentation about the pico command"><code class="unixcommand">pico</code></a>, <a href="http://linux.die.net/man/1/nano" title="click to see detailed documentation about the nano command"><code class="unixcommand">nano</code></a></td>
    <td>crappy but simple text editors (recommended)</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/emacs" title="click to see detailed documentation about the emacs command"><code class="unixcommand">emacs</code></a></td>
    <td>a complicated text editor (not recommended)</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/vi" title="click to see detailed documentation about the vi command"><code class="unixcommand">vi</code></a>, <a href="http://linux.die.net/man/1/vim" title="click to see detailed documentation about the vim command"><code class="unixcommand">vim</code></a></td>
    <td>another complicated text editor (not recommended)</td>
  </tr>

  <tr class="firstrow">
    <th rowspan="2">regular expressions</th>
    <td><a href="http://linux.die.net/man/1/sed" title="click to see detailed documentation about the sed command"><code class="unixcommand">sed</code></a></td>
    <td><span style="text-decoration: underline">s</span>tream <span style="text-decoration: underline">ed</span>itor; find/replace based on regular expressions</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/egrep" title="click to see detailed documentation about the egrep command"><code class="unixcommand">egrep</code></a></td>
    <td>extended version of <code>grep</code> that matches regular expressions</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="2">programming</th>
    <td><a href="http://linux.die.net/man/1/javac" title="click to see detailed documentation about the javac command"><code class="unixcommand">javac</code></a>, <a href="http://linux.die.net/man/1/java" title="click to see detailed documentation about the java command"><code class="unixcommand">java</code></a></td>
    <td>compile or run a Java program</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/python" title="click to see detailed documentation about the python command"><code class="unixcommand">python</code></a>, <a href="http://linux.die.net/man/1/perl" title="click to see detailed documentation about the perl command"><code class="unixcommand">perl</code></a>, <a href="http://linux.die.net/man/1/ruby" title="click to see detailed documentation about the ruby command"><code class="unixcommand">ruby</code></a>, <br> <a href="http://linux.die.net/man/1/gcc" title="click to see detailed documentation about the gcc command"><code class="unixcommand">gcc</code></a>, <code class="unixcommand">sml</code>, ...</td>
    <td>compile or run programs in various other languages</td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="8">shell scripting</th>
    <td><a href="http://linux.die.net/man/1/echo" title="click to see detailed documentation about the echo command"><code class="unixcommand builtin">echo</code></a>, <a href="http://linux.die.net/man/1/printf" title="click to see detailed documentation about the printf command"><code class="unixcommand builtin">printf</code></a></td>
    <td>
      like <code>println</code> for the shell; outputs a message or value
    </td>
  </tr>

  <tr>
    <td><a href="http://linux.die.net/man/1/read" title="click to see detailed documentation about the read command"><code class="unixcommand builtin">read</code></a></td>
    <td>
      reads a value from standard input
    </td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/set" title="click to see detailed documentation about the set command"><code class="unixcommand builtin">set</code></a>, <a href="http://linux.die.net/man/1/unset" title="click to see detailed documentation about the unset command"><code class="unixcommand builtin">unset</code></a></td>
    <td>
      give values to a variable, or delete a variable
    </td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/export" title="click to see detailed documentation about the export command"><code class="unixcommand builtin">export</code></a></td>
    <td>
      sets a variable that any sub-programs launched by this shell can see
    </td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/let" title="click to see detailed documentation about the let command"><code class="unixcommand builtin">let</code></a></td>
    <td>
      for computing integer variable values
    </td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/source" title="click to see detailed documentation about the source command"><code class="unixcommand builtin">source</code></a></td>
    <td>
      executes commands/statements stored in another file <br> 
      (useful for re-loading <code>.bash_profile</code> without logging out)
    </td>
  </tr>
  <tr>
    <td>
      <a href="http://linux.die.net/man/1/if" title="click to see detailed documentation about the if command"><code class="unixcommand builtin">if</code></a>, 
      <a href="http://linux.die.net/man/1/test" title="click to see detailed documentation about the [ command"><code class="unixcommand builtin">[</code></a>,
      <a href="http://linux.die.net/man/1/for" title="click to see detailed documentation about the for command"><code class="unixcommand builtin">for</code></a>,
      <a href="http://linux.die.net/man/1/while" title="click to see detailed documentation about the while command"><code class="unixcommand builtin">while</code></a></td>
    <td>
      <a href="http://linux.die.net/man/1/bash">bash</a> control statements
    </td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/seq" title="click to see detailed documentation about the seq command"><code class="unixcommand">seq</code></a></td>
    <td>
      outputs a sequence of integers (used with <code>for</code> loops)
    </td>
  </tr>
  
  <tr class="firstrow">
    <th rowspan="5">miscellaneous</th>
    <td><a href="http://linux.die.net/man/1/yes" title="click to see detailed documentation about the yes command"><code class="unixcommand">yes</code></a></td>
    <td>output <code>"y"</code> (or another string) over and over</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/sleep" title="click to see detailed documentation about the sleep command"><code class="unixcommand">sleep</code></a>, <a href="http://linux.die.net/man/1/usleep" title="click to see detailed documentation about the usleep command"><code class="unixcommand">usleep</code></a></td>
    <td>pause for a given number of seconds or ms</td>
  </tr>
  <tr>
  <!--	<td><code>~stepp/</code><code class="unixcommand">banner</code></td>
    <td>outputs a message in big letters (on <code>attu</code> only, though you could copy/download it if you are using Linux on a PC)</td> -->
  </tr> 
  <tr>
    <td><code>~stepp/cowsay</code></td>
    <td> displays a talking ASCII cow (on <code>attu</code> only, though you could <a href="http://www.nog.net/~tony/warez/cowsay.shtml">install it</a> if you are using Linux on a PC)</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/xeyes" title="click to see detailed documentation about the xeyes command"><code class="unixcommand">xeyes</code></a></td>
    <td> googley eyes that follow your mouse cursor</td>
  </tr>

  <!--
  lack of arg -> stdin
  ^D to end a "file"
  -->

  <tr class="firstrow">
    <th rowspan="2">build management</th>
    <td><a href="http://linux.die.net/man/1/make" title="click to see detailed documentation about the make command"><code class="unixcommand">make</code></a></td>
    <td>determine which parts of a system must be recompiled, and compile them</td>
  </tr>
  <tr>
    <td><a href="http://linux.die.net/man/1/svn" title="click to see detailed documentation about the svn command"><code class="unixcommand">svn</code></a>, <a href="http://linux.die.net/man/1/cvs" title="click to see detailed documentation about the cvs command"><code class="unixcommand">cvs</code></a></td>
    <td>Subversion and CVS version-control systems</td>
  </tr>
</tbody></table>

# Keyboard Shortcuts
<table>
  <tbody><tr>
    <th>
      key / character
    </th>
    <th>
      description
    </th>
  </tr>

  <tr>
    <td>
      <code>^C</code> or <code>^\</code>
    </td>
    <td>
      kills the currently running process
    </td>
  </tr>

  <tr>
    <td>
      <code>^D</code>
    </td>
    <td>
      end-of-input; press this if a program is reading input from your keyboard and you want to notify it that you are finished
    </td>
  </tr>

  <tr>
    <td>
      <code>^Z</code>
    </td>
    <td>
      suspends (pauses) the currently running process; use <code>fg</code> or <code>bg</code> to resume it
    </td>
  </tr>

  <tr>
    <td>
      <code>^S</code>
    </td>
    <td>
      never ever press this; worst hotkey ever; totally locks up your shell until you press <code>^Q</code>
    </td>
  </tr>
</tbody></table>

