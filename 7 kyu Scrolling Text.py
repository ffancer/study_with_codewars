def scrolling_text(text):
    text = text.upper()
    first_letter = text[0]
    lst = []

    while len(lst) != len(text):
        lst.append(text)
        text = text[1:] + first_letter
        first_letter = text[0]

    return lst


print(scrolling_text("abc"), ["ABC", "BCA", "CAB"])
