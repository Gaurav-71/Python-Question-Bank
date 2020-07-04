dictionary = {}


def names():
    while (tempName := input("Enter name : ")).strip() != "":
        if tempName in dictionary.keys():
            dictionary[tempName] += 1
        else:
            dictionary[tempName] = 1
    for name, count in dictionary.items():
        if count > 1:
            print("There are ", count, "students named", name)
        else:
            print("There is ", count, "student named", name)


names()
