class List:
    def remove_(self, integer_list, values_list):
        for i in values_list:
            while i in integer_list:
                integer_list.remove(i)

        return integer_list


l = List()

integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
values_list = [1, 3]
print(l.remove_(integer_list, values_list), [2, 2, 4])

integer_list = [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8]
values_list = [1, 3, 4, 2]
print(l.remove_(integer_list, values_list), [5, 6, 7, 8])

integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3]
values_list = [2, 4, 3]
print(l.remove_(integer_list, values_list), [8, 7, 6, 5, 1])
