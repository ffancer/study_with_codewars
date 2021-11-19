a == "dev"
b == "Lab"

name == a + b


def fixed_tests():
    def variable_a():
        return (a, 'dev')
    def variable_b():
        return (b, 'Lab')