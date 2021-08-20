def is_anagram(test, original):
    # cnt_test = [i for i in test].sort()
    # cnt_original = [i for i in original].sort()
    #
    # return cnt_test == cnt_original
    check_test = sorted([i.lower() for i in test])
    check_original = sorted([i.lower() for i in original])

    return check_test == check_original



print(is_anagram("foefet", "toffee"), True, 'The word foefet is an anagram of toffee')
print(is_anagram("Buckethead", "DeathCubeK"), True, 'The word Buckethead is an anagram of DeathCubeK')
print(is_anagram("Twoo", "WooT"), True, 'The word Twoo is an anagram of WooT')
print(is_anagram("dumble", "bumble"), False, 'Characters do not match for test case dumble, bumble')
print(is_anagram("ound", "round"), False, 'Missing characters for test case ound, round')
print(is_anagram("apple", "pale"), False, 'Same letters, but different count')

# s = 'MuwmsIrlRibVOw'
# for i in s:
#     print(type(ord(i)))
