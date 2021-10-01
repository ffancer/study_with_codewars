def check_the_bucket(bucket):
    return 'gold' in bucket

print(check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone', ]), True, 'I will bye a teeth')
print(check_the_bucket(['stone', 'stone', 'stone', 'stone', 'stone', ]), False, 'Not today')
print(check_the_bucket(['gold', 'gold', 'gold', 'gold', 'gold', ]), True, 'I will bye a teeth')