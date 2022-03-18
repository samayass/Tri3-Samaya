{% include navigation.html %}

## TT1 - Data Structures 

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@Samayas/Tri3-Samaya-3#week1.py?lite=true"></iframe>

## TT0 - Data Structures project (Menu)
<a href="https://github.com/samayass/Tri3-Samaya">Github</a> <br>

```
from swap import swap1_helper
from matrix import test_matrices


menulist = {
    1: 'Swap',
    2: 'Tree',
    3: 'Matrix',
    4: 'Exit'
}

def printMenu():
    for key in menulist.keys():
        print(key, '--', menulist[key] )
    menu()

def menu():
    while True:
        try:
            option = int(input('Choose one:  '))
            if option == 1:
                a = input("Enter a number")
                b = input("Enter another number")
                print(" ")
                swap1_helper(a, b)
            if option == 2:
                height = int(input('Enter a height:  '))
                for i in range(height):
                    print((' ' * (height - i)) + ('*' * ((2 * i) + 1)))
                print((' ' * height) + '**')
                print((' ' * height) + '**')
            elif option == 3:
                test_matrices()
            elif option == 4:
                print('Exiting')
                exit()
            else:
                print('Invalid input. Enter a number between 1 and 3.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


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
