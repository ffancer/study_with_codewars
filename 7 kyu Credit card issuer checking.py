def get_issuer(number):
    number = str(number)
    if len(number) == 15 and number.startswith('34') or number.startswith('37'):
        return 'AMEX'


print(get_issuer(4111111111111111), 'VISA')
print(get_issuer(378282246310005), 'AMEX')
print(get_issuer(9111111111111111), 'Unknown')
