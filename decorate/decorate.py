def decorater(func):
    def result():
        print("start")
        func()
        print("end")
    return result

@decorater
def decorated_func():
    print("this is test decorate func")


decorated_func()


