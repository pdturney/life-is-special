

What Makes the Game of Life Special?
====================================

Peter Turney
October 10, 2020


Initial Setup
=============

This document describes how to install and run Model-S in Windows 10.
With some changes, you should also be able to run Model-S in Linux
or Mac OS.

(1) Download and Install Golly

Golly is a C++ program for the simulation of cellular automata:

- https://en.wikipedia.org/wiki/Golly_(program)

I used the 64-bit version of Golly 3.3 for Windows 10 
(golly-3.3-win-64bit.zip):

- http://golly.sourceforge.net/
- https://sourceforge.net/projects/golly/files/golly/golly-3.3/
  
Golly is stored in a zip file. I created a directory called Golly64
and put the contents of the zip file in this directory:

- C:\Users\peter\Golly64


(2) Download and Install Python

Golly can be extended with scripts written in Python or Lua. Model-S is
a set of Python scripts that run with Golly.

I used Python 2.7 for Windows. Golly 3.3 is designed to work with Python 2.X
but not Python 3.X. Here is some information on using Python with Golly:

- http://golly.sourceforge.net/Help/python.html


(3) Download and Install Numpy and Statistics

Numpy provides Python numerical functions needed by Model-S. After Python
has been installed, Numpy can be installed in Windows 10 by opening a
command prompt and executing the following commands:

> cd \Python27\Scripts
> pip install numpy
> pip install statistics


Running Code
============

To Execute:

(1) - edit classification_parameters.py to control analysis

(2) - run classification_initialize.py from within Golly.exe
    - this generates a list of rules: all-semitotalistic-rules.txt
    - each rule is assigned a CPU number from 1 to 6

(3) - run classification_main.py from within Golly.exe
    - this creates 6 lists of scores, one for each CPU number
    - run in parallel in 6 separate instances of Golly.exe

(4) - run classification_sort.py from within Golly.exe
    - this merges the 6 lists of scores and sorts them

Example:

- let's say you want to run 3 parallel jobs on 3 CPUs, so that
  the total run time will be one third of the time required
  with 1 CPU
- edit classification_parameters.py as follows:
    num_cpus = 3
    current_cpu_id = 1
- start a copy of Golly running and click on 
  classification_initialize.py
- this will create 3 files, one for each CPU
- assuming the copy of Golly has finished creating
  the files, click on classification_main.py
- this will start the analysis running for all rules
  that are in the file *-CPU1.txt
- now edit classification_parameters.py as follows:
    num_cpus = 3
    current_cpu_id = 2
- start a second copy of Golly running and click on
  classification_main.py
- this will start the analysis running for all rules
  that are in the file *-CPU2.txt
- now edit classification_parameters.py as follows:
    num_cpus = 3
    current_cpu_id = 3
- start a third copy of Golly running and click on
  classification_main.py
- this will start the analysis running for all rules
  that are in the file *-CPU3.txt
- you will now have three copies of Golly running
  in parallel
- when all three copies are done running (which could
  take a day or more, depending on how many rules you
  are using), then run classification_sort.py to merge
  and sort the three files you have generated,
  *-CPU1.txt, *-CPU2.txt, and *-CPU3.txt

