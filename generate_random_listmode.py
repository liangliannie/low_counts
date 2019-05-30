import os
import shutil
import numpy as np
# exefile = "C:\\Users\\z0040tpb\\Desktop\\listmode\\LMBreakout2.exe"
path="/media/liang/LiangPassport/VG50-CUT-Data"
throut = 6.0/8.0

def check_listmode(file):
    if os.path.isfile(file) and '.l' in file and '-List-':
        return True
    return False
def subfolders(fd):
    children=[os.path.join(fd,child) for child in os.listdir(fd)]
    sfs=list(filter(check_listmode, children))
    return sfs

scans=os.listdir(path)
for i in range(len(scans)):
    if '-Converted' not in scans[i] or 'utk' not in scans[i] or 'working' in scans[i]:
        continue
    subpath = os.listdir(os.path.join(path, scans[i]))
    subfolder = list(filter(lambda x: 'LM-00' in x, subpath))[0]
    fd='/'.join([path, scans[i], subfolder])
    file=subfolders(fd)[0] # check CT folders
    print('working on' + file)
    newfile = file[:-2]+'_random_3.l'
    with open(file, 'rb') as f:
        data = np.fromfile(f, dtype='uint64')
    print('origin shape: ', data.shape)
    randomness = np.random.uniform(low=0.0, high=1.0, size=(len(data),))
    newdata = np.extract((data>>31&1) |(randomness>=throut), data) #subfolder
    newdata.tofile(newfile)
    print('saving at'+newfile)
