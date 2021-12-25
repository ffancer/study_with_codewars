def get_issuer(number):
    number = str(number)
    mastercard_tpl = ('51', '52', '53', '54', '55')
    if len(number) == 15 and number.startswith('34') or number.startswith('37'):
        return 'AMEX'
    if len(number) == 16 and number.startswith('6011'):
        return 'Discover'
    if len(number) == 16 and number.startswith(mastercard_tpl):
        return 'Mastercard'


print(get_issuer(4111111111111111), 'VISA')
print(get_issuer(378282246310005), 'AMEX')
print(get_issuer(9111111111111111), 'Unknown')
print(get_issuer(4111111111111111), "VISA")
print(get_issuer(4111111111111), "VISA")
print(get_issuer(4012888888881881), "VISA")
print(get_issuer(378282246310005), "AMEX")
print(get_issuer(6011111111111117), "Discover")
print(get_issuer(5105105105105100), "Mastercard")
print(get_issuer(5105105105105106), "Mastercard")
print(get_issuer(9111111111111111), "Unknown")
