def solve(st,k):
    for i in sorted(st)[:k]:
        st = st.replace(i, '', 1)
    return st

print(solve('abracadabra', 1),'bracadabra')
print(solve('abracadabra', 2),'brcadabra')
print(solve('abracadabra', 6),'rcdbr')
print(solve('abracadabra', 8),'rdr')
print(solve('abracadabra', 50),'')