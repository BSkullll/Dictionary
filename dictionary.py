"""
This is a module of a Dictionary.
A Dictionary that gives the definition of a word.
"""
import json
import difflib
DATA = json.load(open("data.json", 'r'))

def translate(word):
    """
    This Function Takes I/P = Word.
    and gives O/P = Definition of that word.
    :param word:
    :return: Definition of Words. or User friendly Errors
    """
    word = word.lower()
    if word in DATA.keys():
        return DATA[word]

    elif difflib.get_close_matches(word, DATA.keys(), cutoff=0.8):
        value = difflib.get_close_matches(word, DATA.keys(), cutoff=0.8)
        query = input("Do you mean ? {} Enter Y for yes or N for no.".format(value[0]))

        if query == 'Y':
            return DATA[value[0]]

        elif query == 'N':
            return "Thank you"

        else:
            return "You Entered Wrong Option"
    else:
        return f"The word doesn't Exist, Please double check it."

WORDS = input("Enter Your Word : ")
OUTPUT = translate(WORDS)

if isinstance(OUTPUT, list):
    for definition in OUTPUT:
        print(definition)
else:
    print(OUTPUT)
