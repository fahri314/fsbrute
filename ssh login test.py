from paramiko import SSHClient,AutoAddPolicy

hostname = "192.168.47.128"
username = "root"
password = "startx"

def login(hostname, user, password):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    try:
        ssh.connect(hostname, username = username, password = password)
        ssh.close()
        return 1
    except Exception, e:
        return 0
    except KeyboardInterrupt:
        print "\n[-] Aborting...\n"
        file.write("\n[-] Aborting...\n")
        return 0

s = login(hostname, username, password)

print s