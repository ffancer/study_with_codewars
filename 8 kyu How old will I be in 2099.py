# 8 kyu
# How old will I be in 2099?

def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year:
        return f'You are {current_year - year_of_birth} years old.'
    elif current_year < year_of_birth:
        return f'You will be born in {abs(current_year - year_of_birth)} years.'
    elif year_of_birth == current_year:
        return f'You were born this very year!'
    return f'You will be born in {abs(current_year - year_of_birth)} years.'

print(calculate_age(2012, 2016), "You are 4 years old.")
print(calculate_age(1989, 2016), "You are 27 years old.")
print(calculate_age(2000, 2090), "You are 90 years old.")
print(calculate_age(2000, 1990), "You will be born in 10 years.")
print(calculate_age(2000, 2000), "You were born this very year!")
print(calculate_age(900, 2900), "You are 2000 years old.")
print(calculate_age(2010, 1990), "You will be born in 20 years.")
print(calculate_age(2010, 1500), "You will be born in 510 years.")
print(calculate_age(2011, 2012), "You are 1 year old.")
print(calculate_age(2000, 1999), "You will be born in 1 year.")