#!/usr/bin/env python3

def main():
    f = open('alma.txt',"r")
    content = f.read().splitlines()
    for e in content: 
        a=e.split(":")
        
        
    for e in a:
        print(a)
    f.close()
    
if __name__ == "__main__":
    main()