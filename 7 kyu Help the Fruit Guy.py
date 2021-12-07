def remove_rotten(bag_of_fruits):
    try:
        return [i.replace('rotten', '').lower() for i in bag_of_fruits]
    except:
        return []

print(remove_rotten(["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]), ["apple","banana","apple","pineapple","kiwi"])
print(remove_rotten([]), [])