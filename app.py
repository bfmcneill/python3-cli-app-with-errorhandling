import os
from pprint import pprint as pp
import inspect

import err

def main():    
   
    db = get_db_rows() # list of dictionaries

    while True:
        clear_stout()
        print_menu(db)
        user_input = input("\nWhat option would you like to select? or (q)uit ::> ")
        if user_input.lower() == 'q':
            # Quit app
            print("quitting")
            return
        else:
            # app runs here
            if user_input.isdigit():
                # this is where we want the user to get to
                #print("user input a digit")
                #print('user selection >>> {}'.format(user_input))
                idx = int(user_input) - 1
                
                if idx > 0 and idx <= len(db):
                    list_item = db[idx] # returns dictionary
                    pyfunc = list_item.get('pyfunc')
                    
                    try:
                        pyfunc()
                    except Exception as e:
                        print(e)

                else:
                    msg = "Pick a number between 1 and {}".format(len(db))
                    print(msg)
                    
                


            else:
                print("Please input numbers greater than zero")
            
            
            input("Press any key to continue...")



def print_menu(db):        
    """
    Make a selection
    1 - option1
    2 - option2
    3 - option3
    """
   
    print("Make a selection")  
    print("-"*20)  
    for row in db:
        row_num = row.get('row_num')
        title = row.get('title')
        menu_option = "{} - {}".format(row_num, title)
        print(menu_option)
    print()


def clear_stout():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")


def get_db_rows():
    db = [] 
    all_err_functions = inspect.getmembers(err, inspect.isfunction)
    for item_name, item_function in all_err_functions:
        idx = len(db) + 1
        payload = {"row_num":idx, "title":item_name, "pyfunc":item_function}
        db.append(payload)        
        #print(payload)    
    return db

if __name__ == "__main__":
    main()