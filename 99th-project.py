import os
import time
import sys
import shutil
import os.path
from os import path
directory=input("please provide directory path:-")
pathToDelete='/Users/rushil/Documents/Test folder/' + directory
r=os.listdir(pathToDelete)
now=time.time()
for v in r:
     print(path.join(pathToDelete, v))
     print("Current file modified time is:-"+str(os.stat(path.join(pathToDelete, v)).st_mtime))
     n=str(now)
     print("Current UNIX EPOCH TIME:-"+n)
     if((path.exists(path.join(pathToDelete, v))):
         if os.stat(path.join(pathToDelete, value)).st_mtime < now - 7 * 8:
           if path.isfile(value):
             os.remove(path.join(pathToDelete, v))
