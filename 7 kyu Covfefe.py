def covfefe(s):
    return s.replace('coverage', 'covfefe') if 'coverage' in s else s + ' covfefe'


print(covfefe("coverage"), "covfefe")
print(covfefe("coverage coverage"), "covfefe covfefe")
print(covfefe("nothing"), "nothing covfefe")
print(covfefe("double space "), "double space  covfefe")
print(covfefe("covfefe"), "covfefe covfefe")
