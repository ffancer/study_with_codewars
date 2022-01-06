def capital(capitals):
    lst = []

    for i in capitals:
        try:
            lst.append(f"The capital of {i['state']} is {i['capital']}")
        except KeyError:
            lst.append(f"The capital of {i['country']} is {i['capital']}")

    return lst


state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
print(capital(state_capitals), ["The capital of Maine is Augusta"])

country_capitals = [{'country': 'Spain', 'capital': 'Madrid'}]
print(capital(country_capitals), ["The capital of Spain is Madrid"])

mixed_capitals = [{"state": 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital": "Madrid"}]
print(capital(mixed_capitals), ["The capital of Maine is Augusta", "The capital of Spain is Madrid"])
