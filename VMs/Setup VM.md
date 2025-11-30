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


## BlackArch Linux

### Before the first launch

* Download the BlackArch OVA (Will take a while)
* Import the OVA into Virtualbox (Will take a while)
    - Note: The credentials are:
        * Loginname: root
        * Password:  blackarch
* Prepare shared folders with your host:
    - While the machine is turned off, edit and add shared folders to your liking
    - You can specify any mountpoint you like. I like to mount my shares in
      /root/<foldername>.
    - Once you start the machine, your folders should automatically show up in the mount
      path you specified!
* Assign more resources to the machine (RAM, CPU, ...)

### Basic System Configuration

* The machine should start with a welcome screen. Stick with the default desktop env for
  now. Make sure your keyboard layout is chosen correctly! (May need to change layout to
  `de`)
* Login with:
    * Loginname: root
    * Password:  blackarch

* Right click and open a terminal
* If necessary, set your locale permanently: `localectl set-keymap de`

* You will face some issues with pacman in the beginning. The mirrorlist is probably
  outdated, and even though community.db is no longer supported by arch linux it is still found in the blackarch pacman.conf. This
  might prevent you from installing software. How to fix:
    - Edit /etc/pacman.conf and remove the `[Community]` entry and its belonging `Include = ...` directive.
    - Visit https://archlinux.org/mirrorlist/ and generate a mirror list
    - Save the output as a textfile in your shared folder
    - Uncomment some of the servers
    - Copy the file to /etc/pacman.d/mirrorlist
    - Run `pacman -Sy archlinux-keyring` to verify that the mirrors work, and to pull fresh
      keys (otherwise software installs will fail the signature check)

* Most linux systems support CTRL+Shift+C / CTRL+Shift+V for copy pasting in terminals, as
  well as easy movement by holding control and similar. This depends a bit on the terminal
  you use. I personally use urxvt, and for this I need the following change to get these
  features on Black Arch Linux:
    - Edit the /root/.Xdefaults file and add these lines:

        ! Normal copy-paste keybindings without perls
        URxvt.iso14755:                   false
        URxvt.keysym.Shift-Control-V:     eval:paste_clipboard
        URxvt.keysym.Shift-Control-C:     eval:selection_to_clipboard
        !Xterm escape codes, word by word movement
        URxvt.keysym.Control-Left:        \033[1;5D
        URxvt.keysym.Shift-Control-Left:  \033[1;6D
        URxvt.keysym.Control-Right:       \033[1;5C
        URxvt.keysym.Shift-Control-Right: \033[1;6C
        URxvt.keysym.Control-Up:          \033[1;5A
        URxvt.keysym.Shift-Control-Up:    \033[1;6A
        URxvt.keysym.Control-Down:        \033[1;5B
        URxvt.keysym.Shift-Control-Down:  \033[1;6B

        ! Disable the confirmation when pasting stuff with control characters (amongst them \n)
        URxvt.perl-ext: default,-confirm-paste

* If instead of the default desktop, you want to use the i3 wm later, now is a good time
  to copy your i3 config onto the system (through the shared folders). Note that you need
  a different mod key within black arch - I like to use Mod1 (ALT) instead of Windows
  (Mod4) to achieve this necessary separation. Afterwards, you can exit this desktop
  session and continue in i3 if you prefer.


* If you want to configure your system to follow a dark theme globally, there are some
  steps for you to take. The simplest is running:
    * `pacman -Sy gnome-themes-extra`
    * `gsettings set org.gnome.desktop.interface color-scheme prefer-dark`
    * `gsettings set org.gnome.desktop.interface gtk-theme Adwaita-dark`
    * `echo GTK_THEME=Adwaita:dark >> /etc/environment`
    * `echo 'GTK2_RC_FILES=/usr/share/themes/Adwaita-dark/gtk-2.0/gtkrc' >> /etc/environment`
    * Now, after you reboot, you should see that applications such as Firefox
      automatically start in dark theme :)
    * This does not cover ALL applications in the world (qt applications can still be
      annoying...). See https://bbs.archlinux.org/viewtopic.php?id=285066 if you want to
      read more pointers on how to solve the dark mode problem.

* You may face trouble upgrading your black arch system (pacman -Syu) and installing
  up-to-date software due to dependency conflicts. Sadly, this is a direct consequence of
  using the ova or iso images. This wouldn't occur if you had setup a fresh arch
  system with blackarch repos on top of it. The last two year's dependency conflicts have
  to be solved before you can actually install up-to-date packages. These are the steps I used to solve the dependency errors:
    * `pacman -R mobsf tls-attacker rabbitmq scannerl ftpscout pmacct smali backdoor-apk thefatrat python-tensorflow python-gast03 eyeballer python-keras brut3k1t python-mypy python-uvicorn theharvester id-entify rapidscan sn1per python-utidylib powerfuzzer ldapdomaindump aclpwn activedirectoryenum bloodhound-python certipy crackmapexec`
    * `pacman -S jdk-openjdk jdk17-openjdk jdk11-openjdk erlang-eldap python-gast nodejs` (answer yes to all)
    * `pacman -Syu --noconfirm` (this will take quite a while...)
    * Edit `/etc/locale.gen` and comment-out all lines except those for `en_US.UTF-8`
    * Run `locale-gen`

* Some additional software you might want to install (filemanager, dmenu launcher, ...):
    `pacman -Sy nvim pcmanfm dmenu man`

* For vim users: It's recommended to use nvim instead of vim (one example benefit is direct clipboard
  access through the + register). Set an according alias in your .bashrc and .bash_profile:
    `alias vim="nvim"`


* TODO: Does GPU work (e.g. hashcat)?

* TODO: The workaround of upgrading the ova image seems to work initially, but then there
  are issues with the fullscreen view of the VM. Worse yet, the process costs lots of time
  and LOTS of resources (my Blackarch VM Data folder has reached 260GB by now...). Should
  create a blackarch install script based on my normal archlinux netinstall script -> much
  more minimal, won't have all the tools installed when you don't even need them
