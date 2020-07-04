fnames = list(input("Enter List of First names : ").split())
result = []


def partition(list):
    for item in list:
        if 'A' <= item[0] <= 'M' or 'a' <= item[0] <= 'm':
            result.append(item)
    if len(result):
        print("Players whose first name starts with a letter between and including A and M are : ",result)
    else:
        print("There is no player whose first name starts with a letter between and including A and M")


partition(fnames)
