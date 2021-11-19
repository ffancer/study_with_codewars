def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    pass


print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"), "Lew")
print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry"), "Harry")
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"), "Harald")
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"), "Harald")
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"), "Harald")
