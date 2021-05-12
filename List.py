
# Python3 DGallaway 4-28-21 Revision Date:

import random
import secrets

file_name = "Food List.txt"

def add_item(fav_food_list):
    item = input("\nEnter Food to enjoy: ")
    fav_food_list.append(item)

def delete_item(fav_food_list):
    display_list(fav_food_list)
    number = int(input("Which number to delete: "))
    if number < 1 or number > len(fav_food_list):
        print("\nInvalid number!!\n")
    else:
        item = fav_food_list.pop(number - 1)
        print(item + " was deleted/n")

def display_list(fav_food_list):
    print("\nFavorite Foods!!\n")
    size = len(fav_food_list)
    for i in range(0, size):
        print(str(i + 1) + ":" + fav_food_list[i])

def random_food(fav_food_list):
    print("\nRandom Food Pick!\n")
    print(secrets.choice(fav_food_list))


def main():
    print("List of Dinner Ideas!!")

    fav_food_list = []

    choice = 0

    while choice != 5:
        print("\nMenu\n")
        print("1. Add a Food")
        print("2. Delete a Food")
        print("3. List all Foods")
        print("4. Random Food Choice")
        print("5. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_item(fav_food_list)
        elif choice == 2:
            delete_item(fav_food_list)
        elif choice == 3:
            display_list(fav_food_list)
        elif choice == 4:
            random_food(fav_food_list)
        elif choice == 5:
            print("Thank you, Goodbye!!")
        else:
            print("Invalid Selection, pick from the menu!")




if __name__ == "__main__":
    main()
