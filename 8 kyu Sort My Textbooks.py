def sorter(textbooks):
# Cramming before a test can't be that bad?

print(sorter(['Algebra', 'History', 'Geometry', 'English']),
      ['Algebra', 'English', 'Geometry', 'History'], 'Does not sort strings')
print(sorter(['Algebra', 'history', 'Geometry', 'english']),
      ['Algebra', 'english', 'Geometry', 'history'], 'Does not handle capitalization')
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']),
      ['$istory', '**english', 'Alg#bra', 'Geom^try'], 'Does not handle symbols')
