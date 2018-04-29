import module2

def module1func():
    print("module1func")
    print(__file__)
    module2.module2func()

if __name__ == "__main__":
    module1func()
    module1func()
    module1func()
    module1func()
    module1func()
    module1func()
    



