ECHO off
title Component Calculator Installer
ECHO If python is already installed to this machine when the python installer shows please close it however if it is not yet installed please install it.
pause
title Waiting For Python to be Installed
@python-3.8.1-amd64-webinstall.exe
title Extracting Code
@code_extractor.py
ECHO Done!
pause
