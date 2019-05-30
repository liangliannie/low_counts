file = '/home/liang/Desktop/VG50-CUT-Data/60-utk-p01-Converted/60-utk-p01-LM-00/60-utk-p01-LM-00.hdr'
with open(file) as f:
    content = f.readlines()
print(content)
filename = '.l'
newcontent = []
for line in content:
    if line.startswith('name of data file:='):
        line = 'name of data file:=' + filename +'\n'
    newcontent.append(line)


with open('/home/liang/Desktop/VG50-CUT-Data/60-utk-p01-Converted/60-utk-p01-LM-00/60-utk-p01-LM-00_copy.hdr','w') as f:
   f.write(''.join(newcontent))
print('finish')