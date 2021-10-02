def ensure_question(s):
    return s.rstrip('?') + '?'


print(ensure_question(""), "?", "Expected: '?'")
print(ensure_question("Yes"), "Yes?", "Expected: '?'")
print(ensure_question("No?"), "No?", "Expected: '?'")
print(ensure_question("Well????"), "Well????", "Expected: '?'")
