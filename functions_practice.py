def hello():
    print('\nhello\n')
hello()

def pack(item_1, item_2, item_3):
    return [item_1, item_2, item_3]
print(pack("waterbottle", "keys", "wallet"))

def eat_lunch(my_lunch):
    for i in range(0, len(my_lunch)):
        if i == 0:
            print(f"First I eat {my_lunch[i]}")
        else:
            print(f"Next I eat {my_lunch[i]}")
    if len(my_lunch) <= 0:
        print("My lunchbox is empty")

eat_lunch(["a sandwich", "an apple", "my chips"])

