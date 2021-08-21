def capitals(word):
    # first:
    # def capitals(word):
    #     lst = []
    #
    #     for i in range(len(word)):
    #         if word[i].istitle():
    #             lst.append(i)
    #
    #     return lst

    # second:
    return [i for i in range(len(word)) if word[i].istitle()]


print(capitals('CodEWaRs'))
