class Test:
    a = "class_variable_a"
    b = "class_variable_b"

    def __init__(self, a):
        print("Default class variable {}".format(self.a))
        self.a = a
        print("Override default class variable {}".format(self.a))
        self._x = "instance_variable_x"
        print("Created an instance variable {}".format(self._x))
        self.__y = "private_instance_variable__y"
        print("Created a private variable {}".format(self.__y))
        print("Created a private variable {}".format(self._Test__y))
        b = "local_variable_b"
        print("Created a local variable {}".format(self.b))
        print("Created a local variable {}".format(Test.b))
        print("Created a local variable {}".format(b))


def main():
    return


if __name__ == "__main__":
    main()

my_test = Test("main_variable")
print(my_test.a)
print(my_test._x)
print(my_test._Test__y)
print(Test.b)
print(my_test.b)
