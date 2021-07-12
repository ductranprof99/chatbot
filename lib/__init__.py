import subprocess,os,sys

if(not os.path.isdir('./profileFolder')):
    os.mkdir('./profileFolder')
    print('profile Folder created by script')
else:
    print('profile Folder exist')


if(os.path.isfile('./shellscript.ps1')):
    profileFolder = "\'" + os.path.abspath('./profileFolder') + "\'" 
    p = subprocess.Popen(["powershell.exe", "./shellscript.ps1 "+ profileFolder], 
              stdout=sys.stdout)
    p.communicate()
    