* xxd for making hexdumps, and turning hexstrings into binary (echo "hex" | xxd -r -p > output.bin)
* pigz for compressing / decompressing gzip or zlib files

* Archivemount for transparent mounting of archives without fully decompressing them (can
  cause trouble when trying to mount the contents as a loop devices though)

* https://www.exploit-db.com/

* Hydra for brute forcing passwords on online services (e.g. ssh)


* nmap for port scans. You can try scanning across all ports normally with -p- <ip> flag. Later
  when finding open ports, you can perform aggressive scans on only them with -A -p
  22,21 <ip>
