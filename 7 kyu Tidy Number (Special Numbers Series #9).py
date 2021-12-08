def tidyNumber(n):
    n = str(n)
    for i in range(len(n)-1):
        if int(n[i]) < int(n[i+1]):
            continue
        return False
    return True





print(tidyNumber(12), True)
print(tidyNumber(102), False)
print(tidyNumber(9672), False)
print(tidyNumber(2789), True)