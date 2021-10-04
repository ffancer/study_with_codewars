def html_special_chars(data):
    s = ''
    dct = {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        '&': '&amp;'
    }

    for i in data:
        if i in dct:
            s += dct[i]
        else:
            s += i

    return s


print(html_special_chars("<h2>Hello World</h2>"), "&lt;h2&gt;Hello World&lt;/h2&gt;")
print(html_special_chars("Hello, how would you & I fare?"), "Hello, how would you &amp; I fare?")
print(html_special_chars('How was "The Matrix"?  Did you like it?'),
      'How was &quot;The Matrix&quot;?  Did you like it?')
print(html_special_chars("<script>alert('Website Hacked!');</script>"),
      "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;")
