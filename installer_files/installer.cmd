ECHO OFF
title Component Calculator Installer
@python_installed_test
set /p python_test=<python_installed_test_result.txt
if %python_installed%==0 @python-3.8.1-amd64-webinstall.exe
@code_extractor.py
pause
explorer "C:\Component-Calultator\Module-Installers"
ECHO The installation is now fully complete. The program is installed to 'C:\Component-Calculator'.
pause
