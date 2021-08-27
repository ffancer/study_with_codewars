def rental_car_cost(d):
    # first
    # cnt = d * 40
    # if d >= 7:
    #     cnt -= 50
    # elif 7 > d > 3:
    #     cnt -= 20
    # return cnt

    # second
    return d * 40 - 50 if d >= 7 else (d * 40 - 20 if 7 > d > 3 else d * 40)


print(rental_car_cost(1), 40)
print(rental_car_cost(4), 140)
print(rental_car_cost(7), 230)
print(rental_car_cost(8), 270)
