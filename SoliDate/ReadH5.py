import h5py

# 打开H5文件
f = h5py.File('D:\\SoliData\\dsp\\0_0_0.h5', 'r')

# 查看H5文件中的所有组和数据集
print(list(f.keys()))

f.close()