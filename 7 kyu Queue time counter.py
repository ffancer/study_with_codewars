# best practice 1
def queue(queuers,pos):
    return sum(min(queuer, queuers[pos] - (place > pos)) for place, queuer in enumerate(queuers))

# best practice 2
def queue(queuers,pos):
    friendWait = queuers[pos]
    # Divide the line into the front of the line (up to the friend)
    # and back of the line (behind the friend):
    frontOfLine = queuers[:pos+1]
    backOfLine = queuers[pos+1:]
    # Convert the frontOfLine to the min of friendWait:
    frontOfLine = [min(x, friendWait) for x in frontOfLine]
    # Convert the backOfLine to the min of friendWait-1:
    backOfLine = [min(x, friendWait-1) for x in backOfLine]
    # Return the result, which is the sum of both line parts:
    return sum(frontOfLine) + sum(backOfLine)

# best practice 3
def queue(queuers,pos):
    return sum(min(q, queuers[pos]) for q in queuers) - sum(1 for q in queuers[pos + 1:] if q >= queuers[pos])


print(queue([2, 5, 3, 6, 4], 0), 6)
print(queue([2, 5, 3, 6, 4], 1), 18)
print(queue([2, 5, 3, 6, 4], 2), 12)
print(queue([2, 5, 3, 6, 4], 3), 20)
print(queue([2, 5, 3, 6, 4], 4), 17)
