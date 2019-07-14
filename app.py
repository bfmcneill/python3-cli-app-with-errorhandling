import os
from pprint import pprint as pp

def main():    
    clear_stout()
    print_menu()
    

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
    for row in db:
        row_num = row.get('row_num')
        title = row.get('title')
        menu_option = "{} - {}".format(row_num,title)
        print(menu_option)


def clear_stout():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")


if __name__ == "__main__":
    main()