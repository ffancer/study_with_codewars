def tidyNumber(n):
    n = str(n)
    i,j = 0,1

    while j < len(str(n)):
        if int(n[i]) < int(n[j]):
            continue
        i += 1
        j += 1
        return False
    return True





print(tidyNumber(12), True)
print(tidyNumber(102), False)
print(tidyNumber(9672), False)
print(tidyNumber(2789), True)