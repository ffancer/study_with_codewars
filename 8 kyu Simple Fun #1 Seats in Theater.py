# 8 kyu
# Simple Fun #1: Seats in Theater


def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_rows - row) * (tot_cols - (col - 1))


print(seats_in_theater(16, 11, 5, 3), 96)
print(seats_in_theater(1, 1, 1, 1), 0)
print(seats_in_theater(13, 6, 8, 3), 18)
print(seats_in_theater(60, 100, 60, 1), 99)
print(seats_in_theater(1000, 1000, 1000, 1000), 0)
