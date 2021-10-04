def html_special_chars(data):
    dct = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
    return "".join(dct.get(i, i) for i in data)


print(html_special_chars("<h2>Hello World</h2>"), "&lt;h2&gt;Hello World&lt;/h2&gt;")
print(html_special_chars("Hello, how would you & I fare?"), "Hello, how would you &amp; I fare?")
print(html_special_chars('How was "The Matrix"?  Did you like it?'),
      'How was &quot;The Matrix&quot;?  Did you like it?')
print(html_special_chars("<script>alert('Website Hacked!');</script>"),
      "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;")
