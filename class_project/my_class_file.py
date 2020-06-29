class Test:

    def __init__(self, a):
        self._a = a
        self._b = "instance_variable_b"

    @property
    def a(self):
        print("getter of a")
        return self._a

    @a.setter
    def a(self, value):
        print("setter of a")
        self._a = value

    @a.deleter
    def a(self):
        print("deleter of a")
        del self._a

    @property
    def b(self):
        print("getter of b")
        return self._b

    @a.setter
    def b(self, value):
        print("setter of b")
        self._b = value

    @a.deleter
    def b(self):
        print("deleter of b")
        del self._b

def main():
    return


if __name__ == "__main__":
    main()

my_test = Test("main_variable")
print(my_test._a)
my_test._a = "foo"
print(my_test._a)
print(my_test._b)
