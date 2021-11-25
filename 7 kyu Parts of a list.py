def partlist(arr):
    lst = []
    i = 0

    while i < len(arr):
        first = ''.join(arr[i])
        second = ' '.join(arr[i+1:])
        lst.append(first)
        lst.append(second)
        i += 1

    return lst


print(partlist(["I", "wish", "I", "hadn't", "come"]),
      [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"),
       ("I wish I hadn't", "come")])
print(partlist(["cdIw", "tzIy", "xDu", "rThG"]),
      [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")])
print(partlist(["vJQ", "anj", "mQDq", "sOZ"]),
      [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")])
