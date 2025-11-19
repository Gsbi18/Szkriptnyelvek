#!/usr/bin/env python3

class EmptyClass:
    pass    

class MyClass:
    def hello(self):
        return "hello world"
        

def main():
    o= MyClass()
    print(o.hello())


##################################################


if __name__ == "__main__":
    main()
    