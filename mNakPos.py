class NakPosition(object):
    def __init__(self):
        pass

    id = property(lambda self: self.__Id)

    # title = property(lambda self: self.__Title)
    # unit = property(lambda self: self.__Unit)
    # price = property(lambda self: self.__Price)
    # amount = property(lambda self: self.__Amount)
    # summa = property(lambda self: self.__Summa)

    @property
    def _id(self):
        try:
            return self.id
        except AttributeError:
            return None

    # ______________________________________________________________________

    def get_title(self):
        return self.__Title

    def set_title(self, title):
        self.__Title = str(title)

    def del_title(self):
        del self.__Title

    title = property(get_title, set_title, del_title)

    " The old way to make a property "

    @property
    def _title(self):
        try:
            return self.title
        except AttributeError:
            return None

    # ________________________________________________________________________

    @property
    def unit(self):
        return self.__Unit

    @unit.setter
    def unit(self, unit):
        self.__Unit = str(unit)

    @unit.deleter
    def unit(self):
        del self.__Unit

    "The new way"

    @property
    def _unit(self):
        try:
            return self.unit
        except AttributeError:
            return None

    # ________________________________________________________________________

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__Amount = int(amount)

    @amount.deleter
    def amount(self):
        del self.__Amount

    @property
    def _amount(self):
        try:
            return self.amount
        except AttributeError:
            return None

    # __________________________________________________________________________

    @property
    def price(self):
        return self.__Price

    @price.setter
    def price(self, price):
        self.__Price = int(price)

    @price.deleter
    def price(self):
        del self.__Price

    @property
    def _price(self):
        try:
            return self.price
        except AttributeError:
            return None

    # _________________________________________________________________________

    @property
    def summa(self):
        try:
            return self.__Summa
        except AttributeError:
            return self.amount * self.price

    @summa.setter
    def summa(self, summa):
        self.__Summa = (summa)

    @summa.deleter
    def summa(self):
        del self.__Summa

    @property
    def _summa(self):
        try:
            return self.summa
        except AttributeError:
            return None

    # ___________________________________________________________________________

    def __str__(self):
        return "{id}, {title}, {unit}, {price}, {amount}, {summa}".format(
            id=self._id,
            title=self._title,
            unit=self._unit,
            price=self._price,
            amount=self._amount,
            summa=self._summa,
        )

if __name__ == "__main__":
    a = NakPosition()
    print(a)
