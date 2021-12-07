from math import ceil


def movie(card, ticket, rate):
    cnt, total_a, total_b = 0, 0, 0

    while ceil(card + total_b) >= total_a:
        total_a += ticket
        total_b = (total_b + ticket) * rate
        cnt += 1

    return cnt


print(movie(500, 15, 0.9), 43)
print(movie(100, 10, 0.95), 24)
