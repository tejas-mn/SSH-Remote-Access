#!/usr/bin/python3


print("content-type:text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

action=form.getvalue("x")
container_name=form.getvalue("container_name")

if "start" in action:
    cmd=sp.getstatusoutput("sudo docker start {}".format(container_name))
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print()
        print("container {} has started successfully".format(container_name))
        print()
    else:
        print()
        print(output)
        print()

elif "stop" in action:
    cmd=sp.getstatusoutput("sudo docker stop {}".format(container_name))
    status=cmd[0]
    output=cmd[1]

    if status == 0:
        print()
        print("container {} has stopped successfully".format(container_name))
        print()
    else:
        print()
        print(output)
        print()
