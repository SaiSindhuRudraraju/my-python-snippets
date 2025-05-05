class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{{pid = {self.pid}, name = {self.name}, price = {self.price}}}"