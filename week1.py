import swap
import matrix

menu = [
    ["swap", "swap.py"],
    ["keyboard", "matrix.py"],
    ["exit", "c"],
]

if __name__ == "__main__":
    while True:
        for i in range(len(menu)):
            print(menu[i][0])
        print("What would you like")
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


