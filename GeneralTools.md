* xxd for making hexdumps, and turning hexstrings into binary (echo "hex" | xxd -r -p > output.bin)
* pigz for compressing / decompressing gzip or zlib files

* Archivemount for transparent mounting of archives without fully decompressing them (can
  cause trouble when trying to mount the contents as a loop devices though)

* https://www.exploit-db.com/

* Hydra for brute forcing passwords on online services (e.g. ssh)


* nmap for port scans. You can try scanning across all ports normally with -p- <ip> flag. Later
  when finding open ports, you can perform aggressive scans on only them with -A -p
  22,21 <ip>

* To crack passwords:
    - You may want a wordlist as a first try, example: rockyou.txt
    - Blackarch offers a script "wordlistctl" with which you can search and fetch
      wordlists
    - Then you can run tools like pdfcrack (for pdfs) or fcrackzip (zip). Or you could run the
      general-purpose tool john, e.g.:
        - pdf2john <pdffile> > enchash.txt
        - zip2john <zipfile> > enchash.txt
        -  john --wordlist=/usr/share/wordlists/passwords/rockyou.txt enchash.txt
            - NOTE: You can not use the .tar.gz wordlist with john, you must extract it first.
            - sudo tar -xvzf /usr/share/wordlists/passwords/rockyou.txt.tar.gz -C /usr/share/wordlists/passwords 
            - Notably, you CAN use compressed wordlists with hashcat
    - To remove encryption from pdf: pdftk <file> input_pw <pw> output <unencrypted pdf>
    - To open encrypted zip file:
        - 7z x <zipfile> (then enter the password in the prompt)
        - NOTE: unzip -P <password> <zipfile> SHOULD work, but will fail for archives with AES encryption!
* To crack pdf passwords:
    - Use pdfcrack or use pdf2john + john
    - If you find a password, use 
* To crack zip p
