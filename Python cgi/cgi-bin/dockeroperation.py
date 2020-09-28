#!/usr/bin/python3

print("content-type:text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

action=form.getvalue("x")

if "start" in action:
    cmd=sp.getstatusoutput("sudo systemctl start docker")
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print()
        print("docker started sucessfully")
        print()
    else:
        print()
        print(output)
        print()

elif "stop" in action:
    cmd=sp.getstatusoutput("sudo systemctl stop docker")
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print()
        print("docker has stopped successfully")
        print()
    else:
        print()
        print(output)
        print()
if "images" in action:
    cmd=sp.getstatusoutput("sudo docker images ")
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print("Docker Images:\n")
        print(cmd[1])
        print()
    else:
        print()
        print(output)
        print()

elif "re" in action:
    cmd=sp.getstatusoutput("sudo systemctl restart docker")
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print()
        print("docker has restarted successfully")
        print()
    else:
        print()
        print(output)
        print()

if "dockerps" in action:
    cmd=sp.getstatusoutput("sudo docker ps ")
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print()
        print(cmd[1])
        print()
    else:
        print()
        print(output)
        print()
if "status" in action:
    cmd=sp.getstatusoutput("sudo systemctl status docker ")
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print()
        print(cmd[1])
        print()
    else:
        print()
        print(output)
        print()
