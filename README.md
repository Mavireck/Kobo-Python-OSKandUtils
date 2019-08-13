# Kobo-Python-OSKandUtils
A Python On-Screen-Keyboard for Kobo forked from sherman's work in Go. (except now it is in Python, and it is badly-coded)
https://github.com/shermp/go-osk

For a usage example, check the osk_test.py file, or the WolframAlpha app I made.
The 'utils' file include some useful functions which display popups. That may be a good alternative to using telnet to prompt infos from user : you can then just call these function.


It relies on https://github.com/Mavireck/Kobo-Input-Python for input manipulation.
And it MUST be installed at this location : /mnt/onboard/.adds/mavireck/Kobo-Python-OSKandUtils/