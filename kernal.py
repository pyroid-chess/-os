# Essential imports
import os
import re
import sys
import time
import subprocess
from pynput import keyboard   # ✅ using pynput now

# useful functions
def delete_line(): 
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
  
def wait():
    for x in range(0,5):
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)

def wait2(): 
    for x in range(0,5):
        print("-")
        time.sleep(1)
        print("/")
        time.sleep(1)
        print("|")
        time.sleep(1)
        print("\\")
        time.sleep(1)

# boot bios  
base_dir = os.path.dirname(os.path.abspath(__file__))
bios_path = os.path.join(base_dir, "pios", "pi_bios.py")   # adjust if in subfolder
subprocess.run([sys.executable, bios_path])

print("Welcome to π os!\n")
print("Press Esc to exit home screen.")


def pi_cmd_help(page): 
    if page == 1:
        print("/pi.clear.lines\n/pi.app.run.python\n/pi.app.run.c\n/pi.mkdir.internal.storage\n/pi.cd.internal.storage\n/pi.shell.cmd.run\n")

# ✅ Replace keyboard.wait("esc") with pynput
def wait_for_esc():
    def on_press(key):
        if key == keyboard.Key.esc:
            print("Exiting home screen...")
            return False   # stops the listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

wait_for_esc()   # pause here until Esc is pressed

while True:
    user_input = input("π: ")    
    if user_input == "/pi.cmd.help.1" or user_input == "/pi.cmd.help": 
        pi_cmd_help(1)
    elif user_input == "/pi.clear.lines":
        for i in range(0,101):
            delete_line()
    elif user_input == "/pi.app.run.python": 
        app_name = input("π (Python): ")
        app_path = os.path.join("/pios/apps", f"{app_name}.py")
        if os.path.exists(app_path): 
            subprocess.run([sys.executable, app_path])
        else:
            print("Error: cannot run file")
    elif user_input == "/pi.app.run.c":
        app_name = input("π (Clang): ")
        app_path = os.path.join("/pios/apps", f"{app_name}.c")
        output_path = os.path.join("/pios/apps", app_name)  
        if os.path.exists(app_path):
            subprocess.run(["gcc", app_path, "-o", output_path])
            subprocess.run([f"./{output_path}"])
        else:
            print("Error: cannot find C file")
    elif user_input == "/pi.mkdir.internal.storage":  
        dir_name = input("π: ")
        try: 
            os.mkdir(dir_name)
            print("Directory is created")
        except Exception as e: 
            print(f"Error: {e}")
    elif user_input == "/pi.cd.internal.storage":  
        cd = input("π: ")
        try: 
            os.chdir(cd)
        except Exception as e:   # ✅ fixed wrong "error"
            print(f"Error: {e}")
    elif user_input == "/pi.shell.cmd.run":  
        os.system(input("Enter shell command: "))
