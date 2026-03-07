https://www.darkrym.com/posts/2025/06/windows-registry-cheat-sheet/

Hive Name 	Contains 	Location
SYSTEM 	

    Services
    Mounted Devices
    Boot Configuration
    Drivers
    Hardware

	C:\Windows\System32\config\SYSTEM
SECURITY 	

    Local Security Policies
    Audit Policy Settings

	C:\Windows\System32\config\SECURITY
SOFTWARE 	

    Installed Programs
    OS Version and other info
    Autostarts
    Program Settings

	C:\Windows\System32\config\SOFTWARE
SAM 	

    Usernames and their Metadata
    Password Hashes
    Group Memberships
    Account Statuses

	C:\Windows\System32\config\SAM
NTUSER.DAT 	

    Recent Files
    User Preferences
    User-specific Autostarts

	C:\Users\username\NTUSER.DAT
USRCLASS.DAT 	

    Shellbags
    Jump Lists

	C:\Users\username\AppData\Local\Microsoft\Windows\USRCLASS.DAT




Registry Key 	Importance
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist 	It stores information on recently accessed applications launched via the GUI.
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths 	It stores all the paths and locations typed by the user inside the Explorer address bar.
HKLM\Software\Microsoft\Windows\CurrentVersion\App Paths 	It stores the path of the applications.
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery 	It stores all the search terms typed by the user in the Explorer search bar.
HKLM\Software\Microsoft\Windows\CurrentVersion\Run 	It stores information on the programs that are set to automatically start (startup programs) when the users logs in.
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs 	It stores information on the files that the user has recently accessed.
HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName 	It stores the computer's name (hostname).
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
	It stores information on the installed programs.
