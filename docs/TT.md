{% include navigation.html %}

## TT1 - Data Structures 

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@Samayas/Tri3-Samaya-5?lite=true"></iframe>

## TT0 - Data Structures project (Menu)
<a href="https://github.com/samayass/Tri3-Samaya">Github</a> <br>

```
menu = [
    ["swap", "swap.py"],
    ["keyboard", "matrix.py"],
    ["exit", "c"],
]

if __name__ == "__main__":
    while True:
        for i in range(len(menu)):
            print(menu[i][0])
        print("Choose one")
        userInput = input("")

        if userInput == "swap" or userInput == "1":
            a = input("Enter a number")
            b = input("Enter another number")
            print(" ")
            swap.swap1_helper(a, b)
        elif userInput == "keyboard" or userInput == "2":
            print(" ")
            matrix.test_matrices()
        elif userInput == "exit" or userInput == "3":
            exit()
        else:
            print("Enter a valid input")
        print("   ")

```

## TT0 - Data Structures project (Animation)
 
``` 
from time import sleep

def Rocket():
    print(
        """
                   ^
                  / \\
                  |-|
                  | |
                  | |
                  | |
                  | |
                  | |
                 /| |\\
                / | | \\
               |  | |  |
                / | | \\
                /     \\
                -------
        """)

Rocket()

delay = 350
for i in range(10):
    print()
    sleep(delay/1000)
    delay = delay * 1


if __name__ == "__main__":
    Rocket()
```