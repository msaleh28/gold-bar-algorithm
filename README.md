# gold-bar-algorithm

For my algorithm, I used Selenium, a Python package used for web script automation.
I used the provided website http://sdetchallenge.fetch.com/ and wrote an automated script to guess the fake bar. 

To run this program, you must install a Python Conda environment. This is necessary in order to install the Python Selenium package. 

We will need Conda in Python 3.9 to run this program. In your environment, you may follow this website to install (https://saturncloud.io/blog/how-to-install-python-39-with-conda-a-guide-for-data-scientists/).

After successfully installing conda, we will install selenium in the same environment. For this, run terminal command "pip install selenium" and it will do all the hard work for you.

I will provide a short summary for my algorithm. Essentially, I go through each number from 0-7 and weigh them one at a time. For example, my first iteration will be 0 on the left side and 1 on the right side. If not equal, we can determine which is the fake bar by seeing which is lighter. If they are equal, continue. This goes on until the end of the algorithm, where we are left with the last number. If we are able to run through all of the bars and they are all equal, then that must mean the last bar is the fake one by default.

In the case that you are not able to install Conda and Selenium to run this program in your own environment, I am including a YouTube video showcasing how my script works in real time. https://youtu.be/tEY-_7eN7mU 