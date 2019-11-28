import numpy as np

#切片
array=np.random.randint(1,10,16).reshape(4,4)
print(array)
#取出第一行所有值
#print(array[0])
#取出第一列所有值
#print(array[:,0])
#取出第一行和第三行
#print(array[1::2])
#取出第二列和第四列
print(array[::,1::2])
#取出第一行和第三行第二列和第四列
#print(array[0::2,1::2])

#c[2,1] = c[2][1]
#c[1,1,1]=c[1][1][1]