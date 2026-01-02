def func(*arg):
    print(arg)
    print(arg[0])

func(1, 2, 3, 4, 5)
func("a", "b", "c")

def kfunc(**kwargs):
    print(kwargs)
    print(kwargs["name"])

kfunc(name="Alice", age=30)
kfunc(name="New York", country="USA")

