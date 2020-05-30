def say_hi():
    print("hi")


say_hi()


def say_hi(name):
    print("hi", name)


say_hi("steve")


def say_hi(name: object, age: object) -> object:
    print("hi", name, "you're", age)


say_hi("steve", 10)
say_hi("jojo", 15)


def cube(num):
    return pow(num, 3)


print(cube(3))
