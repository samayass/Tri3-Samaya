InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Samaya",
    "LastName": "Sankuratri",
    "FavoriteColor": "Purple",
    "FavoriteSeason": "Winter",
    "Favorite_Foods":["Pizza","Tacos","Seaweed","Grapes", "Chips"]
})

InfoDb.append({
        "FirstName": "Bob",
        "LastName": "Brush",
        "FavoriteColor": "Green",
        "FavoriteSeason": "Summer",
        "Favorite_Foods":["Pasta","Strawberries","Chocolate","Cheese", "Yogurt"]
})

InfoDb.append({
    "FirstName": "Aliya",
    "LastName": "Tang",
    "FavoriteColor": "Blue",
    "FavoriteSeason": "Fall",
    "Favorite_Foods":["Egg","Watermelon","Mac and Cheese","Jello", "Pomegranate"]
})

def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t","Favorite Color: ", InfoDb[n]["FavoriteColor"])
    print("\t","Favorite Season: ", InfoDb[n]["FavoriteSeason"])
    print("\t", "Favorite Foods: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite_Foods"]))  # join allows printing a string list with separator
    print()

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

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

if __name__ == "__main__":
    tester()