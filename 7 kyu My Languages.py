def my_languages(results):
    result = sorted(results.items(), key=lambda t: t[1], reverse=True)
    lst = []

    for i in result:
        if i[1] >= 60:
            lst.append(i[0])

    return lst


print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}),
      ["Ruby", "Python"])
print(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}),
      ["Dutch", "Greek", "Hindi"])
print(my_languages({"C++": 50, "ASM": 10, "Haskell": 20}),
      [])
