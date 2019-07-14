import os
from pprint import pprint as pp

def main():    
    clear_stout()
    while True:
        print_menu()
        user_input = input("\nWhat option would you like to select? or (q)uit ::> ")
        if user_input == 'q':
            # Quit app
            print("quitting")
            return
        else:
            # app runs here
            print('user selection >>> {}'.format(user_input))


def print_menu():        
    """
    Make a selection
    1 - option1
    2 - option2
    3 - option3
    """

    db = []
    row1 = {"row_num":1,"title":"Value Error"}
    db.append(row1)

    row2 = {"row_num":2,"title":"Key Error"}
    db.append(row2)
    
    row3 = {"row_num":3,"title":"KeyBoard Error"}
    db.append(row3)
   
    print("Make a selection")  
    print("-"*20)  
    for row in db:
        row_num = row.get('row_num')
        title = row.get('title')
        menu_option = "{} - {}".format(row_num,title)
        print(menu_option)
    print()


def clear_stout():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")


if __name__ == "__main__":
    main()