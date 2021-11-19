def weather_info(temp):
    celsius = (temp - 32) * (5 / 9)
    if celsius > 0:
        return (str(celsius) + " is freezing temperature")
    else:
        return (str(celsius) + " is above freezing temperature")


# work without it
# def convert_to_celsius(temperature):
#     celsius = (temperature - 32) * (5 / 9)
#     return temperature


print(weather_info(50), '10.0 is above freezing temperature')
print(weather_info(23), '-5.0 is freezing temperature')
