import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))
def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
            suggestion=get_close_matches(word, data.keys())[0]
            print("Did you mean "+suggestion+" ?")
            answer=input("Type Y for yes and N for no: ")
            if answer=="Y" or answer == "y":
                return data[suggestion]
            elif answer=="N" or answer=="n":
                return "The word doesn't exist. Please re-check it."
            else:
                return "Sorry, we did not understand your query."
    else: 
            return "The word doesn't exist. Please re-check it."
    
word = input("Please type the word:")
output = search(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)