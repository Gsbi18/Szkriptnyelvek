#!/usr/bin/env python3

def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")
    
def main():
    greet("Gabi")
    greet("Gabi", greeting="Hola")
    greet("Gabi", greeting="Bonjour")

##################################################


if __name__ == "__main__":
    main()
    