import datetime


def get_villain_name(birthdate):
    first = ["The Evil", "The Vile", "The Cruel", "The Trashy", "The Despicable", "The Embarrassing",
             "The Disreputable", "The Atrocious", "The Twirling", "The Orange", "The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat",
            "Teaspoon", "Laundry Basket"]

    return birthdate.month


format_str = '%d/%m/%Y'  # The format
print(get_villain_name(datetime.datetime.strptime("1/1/2000", format_str)), "The Evil Pickle")
print(get_villain_name(datetime.datetime.strptime("2/2/2000", format_str)), "The Vile Hood Ornament")
print(get_villain_name(datetime.datetime.strptime("2/12/2000", format_str)), "The Awkward Hood Ornament")
