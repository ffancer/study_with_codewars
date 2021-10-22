def partition(arr, classifier_method):
    pass


animals = ["cat", "dog", "duck", "cow", "donkey"]

print(partition(animals, lambda x: len(x) == 3), (['cat', 'dog', 'cow'], ['duck', 'donkey']))