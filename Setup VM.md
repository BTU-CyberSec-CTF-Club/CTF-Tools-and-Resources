# Setting up a VM

## ParrotSec

* On pool PCs:
    - Virtualbox is already installed
    - The ParrotSec OVA is already available at:
        - Windows: CTF Shortcut on the Desktop
        - Ubuntu: /srv/ctf
    - Open Virtualbox and import the OVA image there
        - If the import fails: Uncheck the "Import as VDI Disk" option
* On your own PC:
    - Install Oracle VM Virtualbox: https://www.virtualbox.org/
    - Download the OVA from https://www.parrotsec.org/download/
    - Import the image into virtualbox

* On the first start, the keyboard layout may be off. To fix it:
    - In the start menu search for "Keyboard"
    - Add a new German keyboard layout
    - Delete the US English keyboard layout
    -> everything should work now

* To setup a folder share with your main system:
    - Open the settings of the newly imported ParrotSec Virtual Appliacne ("Ändern" / "Change" with an orange cog icon)
    - Go to Shared Folders and add a new one.
        - Folder path: The path to the folder on your main system
        - Folder name: A name for the share. Preferrably something simple to avoid issues (e.g. "share")
        - Mount point: The mount point within the virtual machine. Can be left empty
        - Make sure "Automatic mount" is checked
    - It makes sense to have a folder share for our CTF Cloud (synced with a cloud
      synchronization client; unless you rather do that within the virtual machine) and
      possibly for our CTF tools repository
    - When you start the machine now, the shares should already be mounted. However, when
      you try to open them, you might run into permission issues. Therefore, add your user
      to the vbox-share group within the virtual machine to gain the permissions:
        - `sudo adduser $USER vboxsf`
        - `sudo gpasswd -a $USER vboxsf`
        - Reboot the VM for changes to take effect
    - If the folders are for some reason not mounted automatically, you can instead setup the automatic mounting yourself by:
        - Creating an executable (chmod +x) file somewhere that runs the following
          command:
            - `mount -t vboxsf -o umask=007,gid=1000,uid=1000 <folder title> <folder mount path>`
            - Ensure that the folder mount path exists, otherwise the mount will fail
        - The executable must be run with sudo on system startup. You can put it in the
          crontab:
            - `sudo crontab -e`
            - Add the line: `@reboot <path to executable>`

