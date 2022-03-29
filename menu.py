# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from week0 import animation, matrix, swap, tree
from week1 import fibonacci, infoDb
from week2 import factorial, GCD, LCM

# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

# Works similarly to main_menu

sub_menu_data = [
    ["Keypad", matrix.test_matrices],
    ["Infodb", infoDb.tester]
]

sub_menu_math = [
    ["Swap", swap.swap1_menu],
    ["Fibonacci", fibonacci.fibonacci_tester],
    ["Factorial", factorial.factorial_tester],
    ["GCD", GCD.GCD_OOP_tester],
    ["LCM", LCM.lcm_tester]
]

sub_menu_adventure = [
    ["Tree", tree.tree],
    ["Pattern", animation.ship]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Data", submenu_data])
    menu_list.append(["Math", submenu_math])
    menu_list.append(["Adventure", submenu_adventure])
    buildMenu(title, menu_list)

def submenu_data():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_data)

def submenu_math():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_math)

def submenu_adventure():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_adventure)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()