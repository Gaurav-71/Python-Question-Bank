fruits = {"apple": 50, "mango": 100, "banana": 20, "orange": 60}
items = list(fruits.keys())
print("Available fruits :- ", items)
getPrice = input("Enter fruit name to get its price : ")
for fruit in list(fruits.keys()):
    if getPrice == fruit:
        print(getPrice, "costs :", fruits[getPrice])
        break
else:
    print("Error: ", getPrice, " can't be found in inventory !")
items.sort()
print("Fruits sorted by name : ", items)
byPrice = dict(sorted(fruits.items(), key=lambda x: x[1]))
print("Fruits sorted by price : ",byPrice)