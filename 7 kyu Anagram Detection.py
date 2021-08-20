def is_anagram(test, original):
    # if len(test) != len(original):
    #     return False

    cnt_test = [test.count(i) for i in test]
    cnt_original = [original.count(i) for i in original]

    # for i in original:
    #     cnt += original.count(i)

    return sum(cnt_test) == sum(cnt_original)

# s = 'apple'
# cnt =0
# for i in s:
#     cnt += s.count(i)
# print(cnt)



print(is_anagram("foefet", "toffee"), True, 'The word foefet is an anagram of toffee')
print(is_anagram("Buckethead", "DeathCubeK"), True, 'The word Buckethead is an anagram of DeathCubeK')
print(is_anagram("Twoo", "WooT"), True, 'The word Twoo is an anagram of WooT')
print(is_anagram("dumble", "bumble"), False, 'Characters do not match for test case dumble, bumble')
print(is_anagram("ound", "round"), False, 'Missing characters for test case ound, round')
print(is_anagram("apple", "pale"), False, 'Same letters, but different count')