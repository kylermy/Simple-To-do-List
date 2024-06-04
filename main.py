"""
Created on Thu May 30 14:42:28 2024

@author: kylermartin
"""


def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Your To-Do List")
    print("2. Add Item to the List")
    print("3. Remove Item from the List")
    print("4. Quit")

def view_list(todo_list):
    print("\nYour To-Do List:")
    for i, item in enumerate(todo_list, start=1):
        print(f"{i}. {item}")

def add_item(todo_list):
    item = input("Enter the item to add: ")
    todo_list.append(item)
    print(f'"{item}" has been added to your list.')

def remove_item(todo_list):
    view_list(todo_list)
    item_num = int(input("Enter the number of the item to remove: "))
    if 1 <= item_num <= len(todo_list):
        removed_item = todo_list.pop(item_num - 1)
        print(f'"{removed_item}" has been removed from your list.')
    else:
        print("Invalid item number.")

def main():
    todo_list = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_list(todo_list)
        elif choice == "2":
            add_item(todo_list)
        elif choice == "3":
            remove_item(todo_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
