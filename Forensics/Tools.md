## Investigating Disk Image files (.img, .img.gz, .iso)

* If you have a .gz image file, start by uncompressing it: gunzip <file>
    - If you don't have the space, there may be solutions to mount and decompress the disk image on the
      fly. However, they are not trivial, so you will need to research

* To find out what a file might be: "file <filename>", e.g. gives info:
    - partition4.img: Linux rev 1.0 ext4 filesystem data, UUID=7a00e9da-98f8-4f0f-b257-95edf422d902 (extents) (64bit) (large files) (huge files)
    - disk.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x2,0,33), end-CHS (0x263,8,56), startsector 2048, 614400 sectors; partition 2 : ID=0x82, start-CHS (0x263,8,57), end-CHS (0x3ff,15,63), startsector 616448, 524288 sectors; partition 3 : ID=0x83, start-CHS (0x3ff,15,63), end-CHS (0x3ff,15,63), startsector 1140736, 956416 sectors
    - If it's a filesystem, you can mount and use your tools on it directly. If it is a
      disk with an MBR / GPT table, you need to isolate the partitions to work on them

* Isolating partitions:
    - Check the partitions on the img: fdisk -l <file>
    - Map the partitions to devices on your system:
        - Automatic: losetup --show -fP disk.img (may need to give --sector-size if sector size differs from default 512)
        - Manual / direct mount of one partition: mount -o ro,loop,offset=<start offset of partition given by fdisk -l> disk.img /mnt


* You can mount valid filesystems (iso, img, ...) with mount: mount -o loop <disk img> /mnt

* Use the tree command to get an overview over files

* Sleuthkit to further investigate file system images. Some example commands:
    - fls -r -m /mnt ./partition4.img > bodyfile  (Generate metadata for all the files in
      the image)
    - mactime -b bodyfile > timeline.txt   (Create an access/modification/creation time
      timeline to overview what happened on the system)
    - icat ./partition4.img 4945 > bcab.dd  (Extract a (corrupted) file's data by inode)
    

* https://unix.stackexchange.com/questions/70684/where-are-sudo-incidents-logged
* https://mcsi-library.readthedocs.io/articles/2022/06/getting-started-with-linux-forensics/getting-started-with-linux-forensics.html

* Steghide for image and audio steganography
* Stegsnow for text-based steganography (adds invisible whitespace)
