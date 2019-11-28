a="age"
xx=lambda x:x[a]
dict = [{"name":"holiday","age":9123},{"name":"1holiday","age":1123}]
dict.sort(key=xx)
print(dict)
