def sorter(textbooks):
    return sorted(textbooks, key=str.lower)


print(sorter(['Algebra', 'History', 'Geometry', 'English']),
      ['Algebra', 'English', 'Geometry', 'History'], 'Does not sort strings')
print(sorter(['Algebra', 'history', 'Geometry', 'english']),
      ['Algebra', 'english', 'Geometry', 'history'], 'Does not handle capitalization')
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']),
      ['$istory', '**english', 'Alg#bra', 'Geom^try'], 'Does not handle symbols')
