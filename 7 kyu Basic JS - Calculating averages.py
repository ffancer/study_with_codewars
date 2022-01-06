class Calculator:
    @staticmethod
    def average(*args):
        try:
            return sum(args) / len(args)
        except:
            return 0


