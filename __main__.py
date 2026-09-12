import sys
import zipfile
import tempfile
import pyfiglet
import subprocess
from check import cj21
print(pyfiglet.figlet_format("javpy - 21"))
if not cj21():
    sys.exit()
a=sys.argv
sp=a.pop(0)
temp=tempfile.TemporaryDirectory()
print("java位于：",temp.name)
with zipfile.ZipFile(sp,"r") as zip:
    zip.extract("java.zip",temp.name)
with zipfile.ZipFile(temp.name+"\\java.zip","r") as zip:
    zip.extractall(temp.name)
a.insert(0,temp.name+"\\bin\\java.exe")
print(a)
subprocess.run(a)
temp.cleanup()
