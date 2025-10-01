#!/usr/bin/env python3

def diamond(height):
    if height % 2 == 0:
        print("Csak páratlan magasságot tudunk feldolgozni, kérlek próbáld újra!!")
        return 1
    
    for i in range(1, height + 1, 2):
        print(("*" * i).center(height))
    for i in range(height - 2, 0, -2):
        print(("*" * i).center(height))
            
            

def main():
    diamond(3)


##################################################


if __name__ == "__main__":
    main()
    