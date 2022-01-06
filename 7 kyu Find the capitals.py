def capital(capitals):
    # your code here
    pass


state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
print(capital(state_capitals), ["The capital of Maine is Augusta"])

country_capitals = [{'country': 'Spain', 'capital': 'Madrid'}]
print(capital(country_capitals), ["The capital of Spain is Madrid"])

mixed_capitals = [{"state": 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital": "Madrid"}]
print(capital(mixed_capitals), ["The capital of Maine is Augusta", "The capital of Spain is Madrid"])
