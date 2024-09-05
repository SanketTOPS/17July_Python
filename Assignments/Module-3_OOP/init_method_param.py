import random

class bank:
    acno=random.randint(11111,99999)
    def __init__(self) -> None:
        print("Account Number:",self.acno)


bn=bank()