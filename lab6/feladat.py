#!/usr/bin/env python3

def loop(n, debug=False,twice=False):
        if debug:
            print("Start loop")
        for e in range(n):
            print((e+1)*2 if twice else e+1)
        if debug:
            print("End loop")

def main():
    loop(5)
    
    loop(5,debug=True)
    loop(5,debug=True,twice=2)
    


##################################################


if __name__ == "__main__":
    main()
    