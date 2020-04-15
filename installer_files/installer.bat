ECHO off
title Showing Instructions
ECHO When installing this program please ensure that python it added to path. As will be shown in the screen shot displayed after you close this message.
pause
title Showing Demo Screen Shot
@install_demo.png
timeout 30
title Waiting For Python to be Installed
@python-3.8.1-amd64-webinstall.exe
title Installing pyshortcuts
pip install pyshortcuts
title Extracting Code
@code_extractor.py
tile Launching Game
@c:\Slimefun-Calculator\launch.bat
