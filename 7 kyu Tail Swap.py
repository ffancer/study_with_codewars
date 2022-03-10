def tail_swap(strings):
    first_head, second_tail = strings[0].split(':')
    second_head, first_tail = strings[1].split(':')
    return [first_head + ':' + first_tail, second_head + ':' + second_tail]


print(tail_swap(['abc:123', 'cde:456']),
      ['abc:456', 'cde:123'])
print(tail_swap(['a:12345', '777:xyz']),
      ['a:xyz', '777:12345'])
