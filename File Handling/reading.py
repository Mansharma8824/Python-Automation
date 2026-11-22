from pathlib import Path
import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(project_dir, "Logs", "device_log.txt")

if file_path:
    with open(file_path, "r") as f :
        print(f.read())
        
else:
    print("file does not exists")
