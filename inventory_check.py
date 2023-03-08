Inventory = []


def searchInventory(thing):
    for i in range(len(Inventory)):
        if Inventory[i][0] == goods[2]:
            return True, i
    return False, -1


def addNum(index, value):
    category = Inventory[index]
    number = int(category[1]) + int(value)
    category = (category[0], number)
    Inventory[index] = category


f = open("inventory_data", "r")
while True:
    fileData = f.readline().strip()
    if fileData == "":
        break
    goods = fileData.split(" ")
    response = searchInventory(goods[2])
    if response[0] == True:
        addNum(response[1],goods[1])
    else:
        Inventory.append((goods[2],goods[1]))


def find_mod():
    mods = [0 for i in range(len(Inventory))]
    for j in range(len(Inventory)):
        mods[j] = int(Inventory[j][1]) % 100
    return mods

product = find_mod()
print(product)

answer = 1
for final in range(len(product)):
    answer = answer * product[final]

print(answer)