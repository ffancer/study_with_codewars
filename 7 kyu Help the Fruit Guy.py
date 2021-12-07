def remove_rotten(bag_of_fruits):
    return [i.replace('rotten', '').lower() for i in bag_of_fruits]


print(remove_rotten(["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]), ["apple","banana","apple","pineapple","kiwi"])
print(remove_rotten([]), [])