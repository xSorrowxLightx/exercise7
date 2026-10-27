#EXERCISE 1

def uses_none(word, evilletters):
    if evilletters in word:
        print("EVIL")
        return False
    else:
        print("all good :)")
        return True

uses_none("hello", "p")

#EXERCISE 2

def uses_only(word, available):
    if available in word:
        print("its in there!")
        return True
    else:
        print("Noap")
        return False

uses_only("hello", "o")

#EXERCISE 3

def uses_all(word, required):
    counter = 0
    for letter in required.lower():
        if letter in word.lower():
            counter += 1
        elif letter not in word.lower():
            return False
    if counter > 0:
        return True
    else:
        return False

print(uses_all("hello", "hel"))

#EXERCISE 4

def check_word(word, sevenletters, required):
    counter = 0
    split_7 = list(sevenletters.lower())    #separates seven letters into a list
    if len(split_7) == 7:                   #if the list has exactly 7 letters, continue
        if required.lower() in word.lower():    #if the required letter is in the word, continue
            for letter in word.lower():         #for every letter in the word
                if letter in split_7:           #if its present in the list of 7 words
                    counter += 1                #add to the counter
                else:
                    print("Not a valid word.")
                    return False                #otherwise, not valid
            if counter > 0:
                print(f"'{word}' is a word that fits all criteria, and is valid!")
                return True
        else:
            print("Does not contain the required letter.")
            return False

    elif len(split_7) < 7:
        print("Not enough letters in the Spelling Bee.")
        return False
    elif len(split_7) > 7:
        print("Too many letters in the Spelling Bee.")
        return False

check_word("color", "ACDLORT", "R")

#that one was complex, but fun
#im not doing the score part :| i already won

#EXERCISE 5, 6, and 7

#uhhhhhhhhhhhhhhhhh

