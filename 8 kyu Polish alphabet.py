# first
def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))

# second
def correct_polish_letters(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i], lt[i])
    return st



print(correct_polish_letters("Jędrzej Błądziński"),"Jedrzej Bladzinski")
print(correct_polish_letters("Lech Wałęsa"),"Lech Walesa")
print(correct_polish_letters("Maria Skłodowska-Curie"),"Maria Sklodowska-Curie")