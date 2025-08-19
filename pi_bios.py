import os
import shutil
import platform
import time

#Wait
def wait(): 
  for x in range(0,5):
    print("-")
    time.sleep(1)
    print("/")
    time.sleep(1)
    print("|")
    time.sleep(1)
    print("\")
    time.sleep(1)
    
#check whether C compiler or C language is installed or not

if shutil.which("gcc"):
  print("GCC compiler is installed....done")
else: 
  print("GCC compiler is not installed")
if shutil.which("clang"):
  print("Clang is installed.....done")
else: 
  print("Clang is not installed")
if shutil.which("cl"):
  print("MSVC (cl.exe) compiler is installed.....done")
else: 
  print("MSVC compiler is not installed")  

if os.path.exists("/pios/apps"): 
  print("Apps folder already created.... done")
else:
  os.mkdir("/pios/apps") 
  print("Apps folder created....done")
  
apps = []
dic = "/pios/apps"
found_apps = {fname: False for fname in apps}
for root,dirs,files in os.walk(dic): 
  for fname in apps: 
    if fname in files: 
      found_apps[fname] = True
      
#checks OS
os_name = platform.system()
print(f"Running {os_name}....done")
wait()
print(f"{os_name}....done")