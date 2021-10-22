def partition(arr, classifier_method):
    lst = list(filter(classifier_method, arr))
    lst2 = []

    for i in arr:
        if i not in lst:
            lst2.append(i)

    return lst, lst2


animals = ["cat", "dog", "duck", "cow", "donkey"]

print(partition(animals, lambda x: len(x) == 3), (['cat', 'dog', 'cow'], ['duck', 'donkey']))
