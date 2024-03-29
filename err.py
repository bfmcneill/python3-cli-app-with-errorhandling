import time


def index_error():
    """Happens when a list item is accessed that does not exist"""
    my_awesome_list = [42, "carrot", len(str(2**50000))]
    print(my_awesome_list[2])
    print(my_awesome_list[4])
    return True


def key_error():
    """normally see this when working with dictionaries"""
    treasure_map = {'lat':34.23,'lon':102.3,'depth':2002}
    print("treasure_map data-type={}".format(type(treasure_map))) # class=dictionary
    print("street_value={}".format(treasure_map.get('street_value')))
    print(treasure_map['street_value']) #error happens here

def function_import_error():    
    from math import sqrt
    print(f"The square root of 36 is ---> {sqrt(36)}")

    from math import sqrootsie
    print("We will never get here")
    
        
def iterator_error():
    # setup
    my_awesome_calculation = len(str(2**50000))
    my_awesome_message = 'If you multiply 2 by itself 50,000 the number will have {} digits'
    my_dogs_favorite_thing = "carrot"
    meaning_of_life = 42
    my_awesome_iterable = [
        meaning_of_life,
        my_dogs_favorite_thing,
        my_awesome_message.format(my_awesome_calculation)
    ]

    my_awesome_iterator = iter(my_awesome_iterable)  

    _type = type(my_awesome_iterable)
    print('The data type for my_awesome_iterable={}'.format(_type))
    
    _type = type(my_awesome_iterator)
    print('The data type for my_awesome_iterator={}'.format(_type))

    print(next(my_awesome_iterator)) #element0 - yes
    print(next(my_awesome_iterator)) #element1 - yes
    print(next(my_awesome_iterator)) #element2 - yes
    print(next(my_awesome_iterator)) #element3 ???  # error occures here

def type_error():    
    print(int('4' + 4))


def value_error():    
    print(int('four'))


def name_error():
    print(int(True))
    print(int(False))
    print(int(true))

def division_error():
    glorious_numeric_value = 1776
    bad_math = glorious_numeric_value / 0 

def keyboard_interrupt_error1():
    """THIS WILL NOT BREAK ON KEYBOARD INTERRUPT"""
    message = {'w':'thats becuase winners never quit','q':'quiters never win'}
    try:
        while True:
            user_choice = input('Are you a (w)inner or a (q)uiter? --> ')               
            user_choice_adj = user_choice.strip()
            if user_choice_adj[0].lower() in message.keys():
                print(message.get(user_choice))
                if user_choice[0].lower() == 'q':                    
                    time.sleep(1.2)
                    break
            else:
                print('that is not acceptable, try again')

    except KeyboardInterrupt:
        print('quiters never win')
    
    except Exception as e:
        print(e)

def keyboard_interrupt_error2():
    """THIS WILL BREAK ON KEYBOARD INTERRUPT"""
    import time
    i=0
    message = "Press Ctrl+C to quit"
    try:
        while True:
            i += 1
            print(i, message)
            time.sleep(1)
    except KeyboardInterrupt:
        print('quitting...')