class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here


EmptyShip = Ship(0, 0)
print(EmptyShip.is_worth_it(), False)