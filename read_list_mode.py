import numpy as np

file ='/home/liang/Desktop/VG50-CUT-Data/60-utk-p01/p01-Data-List-1102.ptd'
data = np.fromfile(file, dtype='uint64')
for d in data:
    print(d)
# print(data)
# randomness = np.random.uniform(low=0.0, high=1.0, size=(len(data),))
# # print((data[:]>>31&1) | (randomness[:]>=0.75))
# newdata = np.extract((data>>31&1) | (randomness>=0.75), data)
# print(data.shape)
# print(newdata.shape)
# print(data, newdata)
