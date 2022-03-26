from week0.swap import swap1_helper
from week0.matrix import test_matrices
from week1.infoDb import tester
from factorial import factorialTester
from week1.fibonacci import fibonacci_tester



menulist = {
    1: 'Swap',
    2: 'Tree',
    3: 'Matrix',
    4: 'InfoDb',
    5: 'Factorial',
    6: 'Fibonacci',
    7: 'Exit'
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
                tester()
            elif option == 5:
                factorialTester()
            elif option == 6:
                fibonacci_tester()
            elif option == 7:
                print('Exiting')
                exit()
            else:
                print('Invalid input. Enter a number between 1 and 3.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    printMenu()