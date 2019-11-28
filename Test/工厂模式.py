class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, type):
        print(self.name, "开始工作了")
        # 使用工厂模式
        axe = Factory.getAxe(type)
        axe.cut_tree()


class Axe(object):
    def __init__(self, name):
        self.name = name

    def cut_tree(self):
        print("使用", self.name, "砍树")


class DJ(Axe):
    def __init__(self):
        pass

    def cut_tree(self):
        print("使用DJ开始砍树")


class StoneAxe(Axe):
    def cut_tree(self):
        print("使用xxx开始砍树")

    def __init__(self):
        pass


class StreeAxe(Axe):
    def __init__(self):
        pass

    def cut_tree(self):
        print("开始yy砍树")


# 创建工厂类
class Factory(object):
    @staticmethod
    def getAxe(type):
        if type == "stoen":
            return StoneAxe()
        elif "stell" == type:
            return StreeAxe()
        elif "DJ" == type:
            return DJ()
        else:
            print("参数有问题")


p = Person("holiday")
p.work("DJ")
