[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=0
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles
[Strings]
InstallPrompt=For this installation to work you must have python and the component calculator installed to this machine. Do you wish to proceed?
DisplayLicense=
FinishMessage=Dev tools module installed successfully. To access it go to 'C:\Component-Calculator\dev_tools' where you can find the manual and the compiling system.
TargetName=C:\Component-Calculator-TEMP\Dev-Tools-Module-Installer.EXE
FriendlyName=Component Calculator Dev Tools Module
AppLaunched=cmd /c "dev_tools_installer.cmd"
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="dev_tools_code_extractor.py"
FILE1="dev_tools_installer.cmd"
FILE2="Dev-Tools-Module-Installer.zip"
[SourceFiles]
SourceFiles0=C:\Component-Calculator-TEMP\
[SourceFiles0]
%FILE0%=
%FILE1%=
%FILE2%=
