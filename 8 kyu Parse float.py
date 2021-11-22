def parse_float(string):
    try:
        return float(string)
    except:
        return None


print(parse_float("1.0"))
print(parse_float("a"))
print(parse_float("234.0234"))
print(parse_float('111'))

string = ['o', '5', 'p', 'n', 'l', 'a', 't', 'u', 'i', 'g', '8', 'f', 'j', 'k', '4', '2', 'a', 'h', '5', 't', '6', 'l',
          'c', 'w', 'u', 'o', 'l', 'b', 'z', '2', 'a', 'c', 'a', 'u', 'h', '5', '.', 'x', '1', '8', 's', 'm', 'o', '5',
          't', 'z', '9', 's', 'v', 'l', 'o', '7', '2', 't', '2', 's', '0', 'v', 'x', '8']
print(parse_float(string))
