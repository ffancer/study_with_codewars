def match(candidate, job):
    return candidate.get('min_salary') * .9 <= job.get('max_salary')


candidate1 = {'min_salary': 120000}
candidate2 = {'min_salary': 190000}
job1 = {'max_salary': 130000}
job2 = {'max_salary': 80000}
job3 = {'max_salary': 171000}

print(match(candidate1, job1), True)
print(match(candidate1, job3), True)
print(match(candidate2, job3), True)

print(match(candidate1, job2), False)
print(match(candidate2, job1), False)
print(match(candidate2, job2), False)

print("Should throw error", lambda a: match({}, job2))

print("Should throw error", lambda a: match(candidate1, {}))
