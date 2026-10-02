class Income:
    def __init__(self, amount, currency="INR"):
        self.amount = float(amount) if amount is not None else 0.0
        self.currency = currency or "INR"

    @classmethod
    def from_dict(cls, data):
        if data is None:
            return cls(0)
        if isinstance(data, cls):
            return data
        if isinstance(data, dict):
            return cls(data.get("amount", 0), data.get("currency", "INR"))
        return cls(data)

    def to_dict(self):
        return {
            "amount": self.amount,
            "currency": self.currency,
        }

    def __float__(self):
        return self.amount

    def __int__(self):
        return int(self.amount)

    def __str__(self):
        return f"{self.currency} {self.amount:,.2f}"


class UserProfile:
    def __init__(
        self,
        role,
        age,
        state,
        education,
        income
    ):
        self.role = role
        self.age = age
        self.state = state
        self.education = education
        self.income = Income.from_dict(income)

    def to_dict(self):
        return {
            "role": self.role,
            "age": self.age,
            "state": self.state,
            "education": self.education,
            "income": self.income.amount,
        }