def covfefe(s):
    if 'coverage' in s:
        return s.replace('coverage', 'covfefe')
    return s + ' covfefe'


print(covfefe("coverage"), "covfefe")
print(covfefe("coverage coverage"), "covfefe covfefe")
print(covfefe("nothing"), "nothing covfefe")
print(covfefe("double space "), "double space  covfefe")
print(covfefe("covfefe"), "covfefe covfefe")
