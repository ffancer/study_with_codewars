def capitals(word):
    # first:
    def capitals(word):
        lst = []

        for i in range(len(word)):
            if word[i].istitle():
                lst.append(i)

        return lst


print(capitals('CodEWaRs'))