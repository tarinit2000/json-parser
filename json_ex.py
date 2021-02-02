import json
# json is easy for humans to read and it's easy for computers to parse through
""" This is a docstring - it is a descriptive message of what this function is and how to use it """
def check_char_count(mystr): # mystr = string
    assert isinstance(mystr, str), 'Input to this function should be a string'
# assert is like a if/else conditional (assert if somehting is true, else print this error message)

    if( len(mystr) == 2):
        return( f'{mystr} count passes')
    else:
        return( f'{mystr} count FAILS' )

def check_char_type(mystr):
    if (mystr.isalpha() and mystr.isupper()):
        return( f'{mystr} type passes' )
    else:
        return( f'{mystr} type FAILS' )

def check_char_match(mystr1, mystr2):
    if(mystr1[0] == mystr2[0]):
        return(f'{mystr1} {mystr2} passes')
    else:
        return(f'{mystr1} {mystr2} FAILS')

def main(): # create a main function with your main code

    with open('states.json', 'r') as f: # load json file into python file
        # f is a file handle that connects to the file states.json and connected under mode "read"
        states = json.load(f) # states = dictionary object 

    for i in range(50):
        #    print(check_char_count( states['states'][i]['abbreviation'] ))
        #   print(check_char_type( states['states'][i]['abbreviation'] ))
        print(check_name_match( states['states'][i]['abbreviation'], states['states'][i]['name']))
        # to see only failures type this into cmd: 
        # python3 json_ex.py | grep "FAIL"

if __name__ == '__main__': #python3 __main__ json_ex.py
    main() # call main function to execute it
