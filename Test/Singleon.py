# 单例模式，则多少实例的对象值相同
class Singleton:
    # 设计实例变量
    __instance = None
    #，如果创建了多个实例，只让init走一次，保证两个对象值为相同
    __First_init = True

    def __init__(self, name):
        if self.__First_init:
            self.__First_init = False
            self.name = name

    # 构造方法
    def __new__(cls,name):
        # 判断实例是否为空
        if not cls.__instance:
            # 如果实例为空，则创建实例
            cls.__instance = object.__new__(cls)
        # 返回实例
        return cls.__instance


s = Singleton("张")
s1 = Singleton("holiday")
print(s.name)
print(s.name)
