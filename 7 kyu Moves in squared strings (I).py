def vert_mirror(strng):
    strng = strng.split('\n')
    return reversed('\n'.join(i[::-1] for i in strng))


def hor_mirror(strng):
    strng = strng.split('\n')
    return '\n'.join(strng[::-1])


def oper(fct, s):
    return fct(s)


print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"),
      "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
print(oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"),
      "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")

print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt")
print(oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK")
