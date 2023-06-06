class Test:
    def __new__(cls, *args, **kwargs):
        print("我是new方法")
        obj = object.__new__(cls)
        print(obj)
        return obj

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self)
        print("我是init方法")

    # def __str__(self):
    #     return "默认调用"

    def __repr__(self):
        return "123"

    def __del__(self):
        print("对象被删除了")

    def __call__(self, *args, **kwargs):
        print("调用了__call__方法")

    def __len__(self):
        return len(self.__dict__)

    def __eq__(self, other):
        print(self.age)
        print(other.age)
        return self.age == other.age

    def __hash__(self):
        return hash(self.name)

if __name__ == '__main__':
    a = Test("1233", 23)
    t = Test("123", 23)
    print(a == t)
    print(len(a))
    print(hash(t))
