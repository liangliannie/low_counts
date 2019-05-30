import os
import shutil
import numpy as np
exefile = "C:\\Users\\z0040tpb\\Desktop\\listmode\\LMBreakout2.exe"
path="F:\\VG50-CUT-Data"
throut = 0.25
scans=os.listdir(path)
def check_listmode(file):
    if os.path.isfile(file) and 'List' in file and '.l' not in file:
        return True
    return False
def subfolders(fd):
    children=[os.path.join(fd,child) for child in os.listdir(fd)]
    sfs=list(filter(check_listmode, children))
    return sfs
for i in range(len(scans)):
    if '-Converted' in scans[i] or 'utk' not in scans[i]:
        continue
    fd=os.path.join(path,scans[i])
    file=subfolders(fd)[0] #check CT folders
    print('working on ' + file)
    newfile = file[:-3]+'l'
    newfile.replace('List-', '')
    save_header = exefile + '  -f '+ file + ' -d '+fd+'\\header'+ ' -x'
    os.system(save_header)
    generate_listmode = 'copy '+ file + ' ' + newfile
    os.system(generate_listmode)
    putback_header = exefile + '  -f '+ file + ' -a '+fd+'\\header'
    os.system(putback_header)
