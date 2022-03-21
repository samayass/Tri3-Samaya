{% include navigation.html %}

## Runtime

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@Samayas/Tri3-Samaya-3?lite=true"></iframe>

## TT1 - Lists and Loops

### Lists and loops to display
```
InfoDb.append({
    "FirstName": "Samaya",
    "LastName": "Sankuratri",
    "FavoriteColor": "Purple",
    "FavoriteSeason": "Winter",
    "Favorite_Foods":["Pizza","Tacos","Seaweed","Grapes", "Chips"]
})
```
```
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

## hack 2b: def while_loop(0)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

## hack 2c : def recursive_loop(0)
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return
    
```

## Fibonacci 

```
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)
```







## TT0 - Menu and Animation

### Menu
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

### Animation
 
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
