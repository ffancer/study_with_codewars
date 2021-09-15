def calc_type(a, b, res):
    return {
        a + b: "addition",
        a - b: "subtraction",
        a * b: "multiplication",
        a / b: "division"
    }[res]


print(calc_type(1, 2, 3), "addition")
print(calc_type(10, 5, 5), "subtraction")
print(calc_type(10, 4, 40), "multiplication")
print(calc_type(9, 5, 1.8), "division")