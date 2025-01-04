import subprocess
import os


var = subprocess.run('netstat -a', shell=True, capture_output=True, text=True, timeout=1)
#Returns: CompletedProcess(args='tree', returncode=0)

with open('python.txt', 'wt+') as file:
    file.write(str(var.stdout))

print(f'{var}\n{type(var)}')
