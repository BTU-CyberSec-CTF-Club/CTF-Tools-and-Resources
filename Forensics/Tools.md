* To find out what a file might be: "file <filename>", e.g. gives info
    partition4.img: Linux rev 1.0 ext4 filesystem data, UUID=7a00e9da-98f8-4f0f-b257-95edf422d902 (extents) (64bit) (large files) (huge files)
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
