
class Transaction:
    def __init__(self, amount, date, category, type_):
        self.amount = amount
        self.date = date
        self.category = category
        self.type_ = type_

    def __str__(self):
        return f"{self.date} - {self.category} - {self.type_} - {self.amount}"
