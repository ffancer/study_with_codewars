def echo_program():
    return open(__file__).read()


print(isinstance(echo_program(), str))