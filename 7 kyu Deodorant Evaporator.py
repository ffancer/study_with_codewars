def evaporator(content, evap_per_day, threshold):
    percentage = 100
    result = 0
    while percentage > threshold:
        percentage = percentage - percentage * (evap_per_day / 100)
        result += 1

    return result

print(evaporator(10, 10, 10), 22)

