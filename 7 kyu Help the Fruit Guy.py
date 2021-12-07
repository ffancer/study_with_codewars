def remove_rotten(bag_of_fruits):
    if type(bag_of_fruits) is None or len(bag_of_fruits) == 0:
        return []
    return [i.replace('rotten', '').lower() for i in bag_of_fruits]


print(remove_rotten(["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]), ["apple","banana","apple","pineapple","kiwi"])
print(remove_rotten([]), [])