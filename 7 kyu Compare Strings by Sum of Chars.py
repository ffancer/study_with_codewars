def compare(s1,s2):
    pass


print(compare("AD", "BC"), True, "\'AD\' vs \'BC\'")
print(compare("AD", "DD"), False, "\'AD\' vs \'DD\'")
print(compare("gf", "FG"), True, "\'gf\' vs \'FG\'")
print(compare("Ad", "DD"), False, "\'Ad\' vs \'DD\'")
print(compare("zz1", ""), True, "\'zz1\' vs \'\'")
print(compare("ZzZz", "ffPFF"), True, "\'ZzZz\' vs \'ffPFF\'")
print(compare("kl", "lz"), False, "\'kl\' vs \'lz\'")
print(compare(None, ""), True, "\'<null>\' vs \'\'")
print(compare("!!", "7476"), True, "\'!!\' vs \'7476\'")
print(compare("##", "1176"), True, "\'##\' vs \'1176\'")