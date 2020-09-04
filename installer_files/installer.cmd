ECHO OFF
title Component Calculator Installer
@python_installed_test.py
set /p python_test=<python_installed_test_result.txt
if %python_test%==0 @python-3.8.1-amd64-webinstall.exe
@code_extractor.py
ECHO The installer will now open the folder containing all the installer files for different optional databases and modules. Please note that if this is the first version after a major update (for example 3.0.0) it is unlikely any databases are included as the update would have meant they need to be modified.
pause
explorer "C:\Component-Calultator\Module-Installers"
ECHO The installation is now fully complete. The program is installed to 'C:\Component-Calculator'.
pause
