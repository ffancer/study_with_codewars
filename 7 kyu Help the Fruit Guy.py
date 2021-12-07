def remove_rotten(bag_of_fruits):
    lst = []

    for i in bag_of_fruits:
        lst.append(i.replace('rotten', '').lower())

    return lst


print(remove_rotten(["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]), ["apple","banana","apple","pineapple","kiwi"])
print(remove_rotten([]), [])