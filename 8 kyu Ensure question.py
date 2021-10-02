def ensure_question(s):
    return s if s.endswith('?') else s + '?'


print(ensure_question(""), "?", "Expected: '?'")
print(ensure_question("Yes"), "Yes?", "Expected: '?'")
print(ensure_question("No?"), "No?", "Expected: '?'")
print(ensure_question("Well????"), "Well????", "Expected: '?'")
