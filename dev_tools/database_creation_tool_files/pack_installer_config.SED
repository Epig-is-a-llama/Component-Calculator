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
InstallPrompt=For this installation to succeed both the Component-Calculator and python must be installed to this machine. If both are installed click yes if either is not please click no and then install them.
DisplayLicense=
FinishMessage=Finished installing this database!
TargetName=C:/Component-Calculator/dev_tools/compiled_databases/Dreadark-database-installer.EXE
FriendlyName=Database Installer
AppLaunched=cmd /c "database_package_installer.cmd"
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="C:\Component-Calculator\dev_tools\database_creation_tool_files\database_package_installer.cmd"
FILE1="C:\Component-Calculator\dev_tools\database_creation_tool_files\database_extractor.py"
FILE2="C:\Component-Calculator\dev_tools\database_creation_tool_files\database.zip"
[SourceFiles]
SourceFiles0=
[SourceFiles0]
%FILE0%=
%FILE1%=
%FILE2%=
