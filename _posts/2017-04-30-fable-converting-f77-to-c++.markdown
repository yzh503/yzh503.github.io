---
layout: post
title: fable - Automatic Fortran to C++ conversion
date: 2017-04-30 
author: Simon
comments: true
summary: Converting Fortran to C++
categories: programming language
tags: 
 - fortran
 - c++
---
# Why converting Fortran to C++
Many legacy Fortran programs are still stable and running in the industry. It is often difficult to maintain and extend the legacy code (well, difficult compared with modern languages). I was developing an extension on a Fortran 77 program, but F77 does not support many important modern programming features, which really gave me a hetic. Converting old Fortran to C/C++, it is hoped that we can use C++ features to extend an old program, although it would not improve the readibilty of code at all. 

In this article commands are executed in Linux/Unix environment.

# Things you need
1. Install fable converter following the steps on the [official website](http://cci.lbl.gov/fable/)
2. Download the [cctbx library](https://github.com/cctbx/cctbx_project), in case if the included library lacks files)

# Convert Fortran to C++
Don't forget to source cctbx_env.sh
{% highlight shell %}
source <installation directory>/cctbx-dev-<version>/cctbx_env.sh
{% endhighlight %}
Use fable to convert a .f file to a C++ source file
{% highlight shell %}
fable.cout code.f --namespace=code > code.cpp
{% endhighlight %}
The converter does not automatically “link” external functions. Placeholders of missing functions will be generated in absence of external function definition. The converted C++ code needs to be modified manually to replace the body of the external function with the real implementation. You may convert multiple Fortran files to one C++ file and sequentially separate C++ funtions to different files. Included files in Fortran will be automatically detected. 

# Problems
Equivalence and common vairables are commonly used for shared resources in Fortran 77. With fable version 1022, no more than 7 equivalent variables are allowed in conversion, that is, a common variable cannot have more than 7 symbols. 

The following code is convertible
{% highlight fortran %}
      dimension arr1(10), arr2(10)
      equivalence (arr1, arr2)
c calculate squares from 1 to 10
      do 100 i = 1, 10
        arr1(i) = i**2
  100 continue
c print the 10 numbers
      do 200 i = 1, 10
        write(*,*) arr2(i)
  200 continue
      end
{% endhighlight %}   

The following code is currently inconvertible
{% highlight fortran %}
      dimension arr1(10), arr2(10), arr3(20), arr4(10)
      dimension arr5(20), arr6(20), arr7(20), arr8(20), arr9(20)
      equivalence (arr1, arr2)
      equivalence (arr2, arr3)
      equivalence (arr3, arr4)
      equivalence (arr4, arr5)
      equivalence (arr5, arr6)
      equivalence (arr6, arr7)
      equivalence (arr7, arr8)
      equivalence (arr8, arr9)
      do 100 i = 1, 10
          arr1(i) = i**2
  100 continue
      do 200 i = 1, 10
         write(*,*) arr9(i)
  200 continue
      end
{% endhighlight %}

One solution is to reduce the number of equivalence in Fortran before conversion.

