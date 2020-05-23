import json
from difflib import get_close_matches

'''Simple program that checks meaning of words from a json file and
and returns the meaning as given in the json file.
'''

file = json.load(open("data.json"))

def checker(x):
    if x.lower() in file :
        return file[x]
    elif x.upper() in file:
        return file[x.upper()]
    elif x.title in file:
        return file[x.title()]
    elif len(get_close_matches(x, file.keys())) > 0 :
        conf =  input("Did you mean %s instead? Y/N : " %get_close_matches(x,file.keys())[0])
        if conf == 'Y' or 'y':
            return file[get_close_matches(x,file.keys())[0]]
        else:
            return "Query not found "
    else:
        return "Word does not exist"

#print(checker(x))
while True:
    x = input("Enter the word to be searched or 'clc' to exit : ")
    if x == 'clc':
        break
    else:
        print(checker(x))
