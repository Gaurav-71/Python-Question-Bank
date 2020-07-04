exitLoop = False
dictionary = {}

def create(newWord, meaning):
    dictionary[newWord] = meaning
    print(newWord, "has been added !")


def search(key):
    if key in dictionary.keys():
        print(key, "found and its meaning is : ", dictionary[key])
    else:
        print(key, "is not defined in dictionary")


def synonym(keyMeaning):
    synonyms = [word for word, meaning in dictionary.items() if meaning == keyMeaning]
    if len(synonyms):
        print("Synonyms found were", synonyms)
    else:
        print("No synonyms were found for", keyMeaning)


def delete(word):
    if word in dictionary.keys():
        del dictionary[word]
        print(word, " has been deleted from dictionary")
    else:
        print(word, "not found !")


def display():
    words = list(dictionary.keys())
    words.sort()
    print("Words in sorted order : ", words)


while not exitLoop:
    print("\n\n1. New word\n2. Search word\n3. Find Synonyms\n4. Delete word\n5. Display\n6. Exit")
    choice = int(input("\n-> Choice : "))
    if choice == 1:
        print("\nAdd a new word :-")
        create(input("Enter new word : "), input("Enter word meaning : "))
    elif choice == 2:
        print("\nSearch dictionary :-")
        search(input("Enter the word you want to search"))
    elif choice == 3:
        print("\nSynonyms :-")
        synonym(input("Enter meaning to find the word(s) : "))
    elif choice == 4:
        print("\nDelete word :-")
        delete(input("Enter word to delete : "))
    elif choice == 5:
        print("\nDisplay :-")
        display()
    else:
        exitLoop = True
