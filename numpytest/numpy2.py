import  numpy as np
a1 =  np.random.randint(1,10,9).reshape(3,3)
a2=np.ones(9).reshape(3,3)
#数组合并，将所有数组的值合并成一个数组
#print(a1.ravel())
#两个矩阵合并
#print(np.vstack((a1,a2)))
#在a1矩阵中每个数组后面拼接a2矩阵
#print(np.hstack((a1,a2)))
#print(np.row_stack((a1,a2)))
#print(np.column_stack((a1,a2)))

#拆分 相当于spark,repartition
#print(np.stack((a1,a2),2))
#切割
print(np.split(a1,3))
print(np.vsplit(a1,3))
