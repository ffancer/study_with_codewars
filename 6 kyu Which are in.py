# 6 kyu
# Which are in?


def in_array(array1, array2):
    lst = []
    for i in array1:
        for j in array2:
            print(i, j)


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1, a2))
a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp']
print(in_array(a1, a2))
