import json
from difflib import get_close_matches

msg = "The word doesn't exist. Please double check it."

#Loading the json data
data = json.load(open("data.json"))

#Returning the definition of a word
def translate(word):
    word = word.lower()  #accounting for case sensitivity
    if word in data:
        return data[word]
    elif word.tittle() in data:
        return data[w.tittle()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(data.keys())[0]]
        elif yn == "N":
            return msg
        else:
            return "We didn't understand your entry."
    else:
        return msg
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
