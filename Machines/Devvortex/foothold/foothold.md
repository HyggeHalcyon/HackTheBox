## Foothold

### Information Disclosure
[CVE-2023-23752](https://github.com/Acceis/exploit-CVE-2023-23752) 

### RCE
[Hacktricks-Joomla](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/joomla#rce)
- Go to administrator templates
- edit error.php to call system revshell
- access `http://dev.devvortex.htb/administrator/templates/atum/error.php` to execute it 