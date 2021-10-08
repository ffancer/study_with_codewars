def cube_checker(volume, side):
    pass


print(cube_checker(-12,2), False)
print(cube_checker(8, 3),  False)
print(cube_checker(8, 2),  True)
print(cube_checker(-8,-2), False, "side or volume < 0 are invalid !")
print(cube_checker(0, 0),  False)
print(cube_checker(27, 3), True)
print(cube_checker(1, 5),  False)
print(cube_checker(125, 5),True)
print(cube_checker(125,-5),False)
print(cube_checker(0, 12), False)
print(cube_checker(12, -1),False)
print(cube_checker(1, 1),  True)