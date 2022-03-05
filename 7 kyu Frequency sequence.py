def freq_seq(s, sep):
    ans = ''

    for i in s:
        ans += str(s.count(i)) + sep

    return ans[:-1]


print(freq_seq('hello world', '-'), '1-1-3-3-2-1-1-2-1-3-1')
print(freq_seq('19999999', ':'), '1:7:7:7:7:7:7:7')
print(freq_seq('^^^**$', 'x'), '3x3x3x2x2x1')
