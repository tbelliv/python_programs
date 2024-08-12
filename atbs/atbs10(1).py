from pathlib import Path
myfiles = ['accounts.csv','customers.csv','notes.txt']
for file in myfiles:
    print(Path(r'/home/timot',file))