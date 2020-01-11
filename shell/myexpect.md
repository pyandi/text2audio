# myexpect

> Expect script to connect to a remote server and execute command.

**This script needs two part arguments**:

- part I: password = Password of username the remote server.
- part II command = you will execute command in the remote server.

## example

 ```shell
#non-interactive ssh
./myexpect password ssh root@192.168.1.1
./myexpect password ssh -p 2222 root@192.168.1.1

#non-interactive scp
./myexpect password scp root@192.168.1.1:/tmp/test .
./myexpect password scp root@192.168.1.1:/tmp/test /tmp/test
./myexpect password scp /tmp/test root@192.168.1.1:/tmp/test
./myexpect password scp -P 2222 root@192.168.1.1:/tmp/test .

#non-interactive execute command on the remote server.
./myexpect password ssh -p 2222 root@192.168.1.1 df -h
./myexpect password ssh -p 2222 root@192.168.1.1 free -m
./myexpect password ssh -p 2222 root@192.168.1.1 mv -f file1 file2
./myexpect password ssh -p 2222 root@192.168.1.1 cp -f file1 file2
```
