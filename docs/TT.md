{% include navigation.html %}

[TT0](#tt0)
[TT1](#tt1)
[TT2](#tt2)
[TT3](#tt3)


## Runtime

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@Samayas/Tri3-Samaya-3?lite=true"></iframe>


## <a name="tt3"></a>TT2 - Accounts and Login

### Hack 1 - Add Phone Number to Sign Up screen
<img width="312" alt="picture" src="https://user-images.githubusercontent.com/89225474/163730825-1d949341-1c85-43b1-9c02-b214d81f4d12.png">

``` phone = request.form.get("phone") ``` <br>
``` "phone": self.phone, ```<br>

### Hack 2 - Add logout to CRUD screen. Display logged in User on top of CRUD Page
<img width="901" alt="picture" src="https://user-images.githubusercontent.com/89225474/163731105-7974c4db-cbef-4eaa-87b0-de36b44b4377.png">

``` 
<div class='parent'>
    <div class='child'><h1 style="">Current User: {{ current_user.name }}</h1></div>
    <div class='child'><button><a href={{url_for('crud.crud_logout')}}>Log out</a></button></div>
</div>
```
### Hack 3 - Add login_required to another portion of project


```
@tennis_pg.route('/photos/')
@login_required
def photos():
    return render_template("photos.html")
```






## <a name="tt2"></a>TT2 - Python Classes

### GCD with OOP
```
class GCD:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self):
        # return 0 for the GCD if one of the inputs is 0
        if self.a==0:
            return 0
        # return 0 for the GCD if one of the inputs is 0
        if self.b==0:
            return 0
        #  checking if the two inputs evenly divide
        if self.a % self.b ==0:
            return self.b
        if self.b % self.a ==0:
            return self.a
        # subtract smaller input from larger input. Replace larger value with difference and recursively call
        if self.a > self.b:
            self.a = self.a -self.b
            return self()
        if self.b > self.a:
            self.b = self.b - self.a
            return self()
```


### Factorial with OOP

```
class factorial:
    def __init__(self):
        self.factorial = [0, 1]

    def __call__(self, n):
        if n < len(self.factorial):
            return self.factorial[n]
        else:
            # Compute the requested Fibonacci number
            fac_number = n * self(n-1) # two recursive calls to self (__call__(self, n))
            self.factorial.append(fac_number)
        return self.factorial[n]

```


## <a name="tt1"></a>TT1 - Lists and Loops

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

## <a name="tt0"></a>TT0 - Menu and Animation

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
