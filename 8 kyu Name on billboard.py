def billboard(name, price=30):
    cnt = 0

    for i in range(len(name)):
        cnt += 1

    return cnt * price

print(billboard("Jeong-Ho Aristotelis"), 600)
print(billboard("Abishai Charalampos"), 570)
print(billboard("Idwal Augustin"), 420)
print(billboard("Hadufuns John", 20), 260)
print(billboard("Zoroaster Donnchadh"), 570)
print(billboard("Claude Miljenko"), 450)
print(billboard("Werner Vigi", 15), 165)
print(billboard("Anani Fridumar"), 420)
print(billboard("Paolo Oli"), 270)
print(billboard("Hjalmar Liupold", 40), 600)
print(billboard("Simon Eadwulf"), 390)
