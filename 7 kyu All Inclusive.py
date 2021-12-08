# 7 kyu
# All Inclusive?

def contain_all_rots(strng, arr):
    return False if strng not in arr and arr.count(strng) != 1 else True


print(contain_all_rots("", []), True)
print(contain_all_rots("", ["bsjq", "qbsj"]), True)
print(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)
print(contain_all_rots("XjYABhR",
                       ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR",
                        "ABhRXjY"]), False)
