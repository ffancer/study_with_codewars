def weather_info(temp):
    c: convert(temp)
    if (c > 0):
        return (c + " is freezing temperature")
    else:
        return (c + " is above freezing temperature")


def convert_to_celsius(temperature):
    var celsius = (tempertur) - 32 + (5 / 9)
    return temperature


print(weather_info(50), '10.0 is above freezing temperature')
print(weather_info(23), '-5.0 is freezing temperature')