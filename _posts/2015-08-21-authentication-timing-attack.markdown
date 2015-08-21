---
layout: post
title: Authentication Timing Attack
date: 2015-08-21
author: yzh503
summary: Get the password of web authentication.
categories: Web_Penetration
tags: 
 - Web penetration
 - Authentication Timing Attack
---

##Background 
Non-constant string comparison time is a vulnerablity of web authentication. If a web developer did not set up constant response time, attackers may get the password by comparing response time of requests. In this article, we will use [Web for Pentester II](https://pentesterlab.com/exercises/web_for_pentester_II) authentication exercise 2 as an example. 

##Basics
![auth page](http://theimagehost.net/upload/a1a7047fe4a55636d6a11fd3cdc26dd4.png)
The process of authenticating is as the following:  
1. The browser sends a HTTP authentication request.     
2. The server compares the strings, and sends response.  

There are different types of auth requests, such as Basic, Digest, and custom authentication. The username and password are concealed in the HTTP header. This is the header of Basic Authentication, which is the type of authentication in this example.
{% highlight html %}
GET /authentication/example2 HTTP/1.1
Host: http://192.168.56.101
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
{% endhighlight %}
"dXNlcm5hbWU6cGFzc3dvcmQ=" is the base64 code of "username:password". The response will give you the status, which is whether you are authenticated or not, and some other content. Status code 200 is success, and 401 is fail. 


##How to
Suppose the actual password is "abcde". Comparing "abcde" with "ab123" and "abc123", the second one takes more time than the first one. The first one compares 3 characters, and stops at the third letter. The second one compares 4 letters, and stops at the fourth character. Based on this time difference, you could get the correct characters one by one, by comparing the response time of the auth requests. 


##Details
Write a script to send authentication requests, and jot down the response time automatically. For example, this is a part of my ouput.
{% highlight html%}
$ python ex2.py
 0 0 1.408078
 1 1 1.408148
 2 2 1.408747
...
23 n 1.408357
24 o 1.408269
25 p 1.609422
26 q 1.407573
27 r 1.406407
...
--------------------
Suggest:  25
Select one: 25
...
 1 p1 1.607937
 2 p2 1.608372
 3 p3 1.607752
 4 p4 1.810275
 5 p5 1.608626
 6 p6 1.609457
...
--------------------
Suggest:  4
Select one: 4
...
 0 p40 1.809672
 1 p41 1.810446
 2 p42 1.808867
...
{% endhighlight %}
The format follows "Index password response_time". In the first loop, I sent requests with one character as password. "p" took longer to respond, which indicated that p is likely to be contained in the password. With the correct bit confirmed, we can then test on next bit. To make the script more reliable and stable, it is better to be able to select each character manually, and even go back. It has to stop when it finds the correct password (getting response 200). 


###Script 
For this example, I used python to send requests and count time. Requests: HTTP for Humans is an amazing library for HTTP request. You can write extremely simple neat code to send requests with this library. time.time() can be used to measure the response time. Note that time.clock() and time.time() is different. clock() counts the processing time with respect to the CPU clock, while time() counts the local time, including network latency.
