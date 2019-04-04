import mDocument
import mNakPos


def create():
    return Nakladnaya(status=mDocument.Document.New)


class Nakladnaya(mDocument.Document):
    def __init__(self, **kwargs):
        self.__Itogo = 0
        mDocument.Document.__init__(self, **kwargs)
        self.__Positions = []

    itogo = property(lambda self: self.__Itogo)

    @property
    def _itogo(self):
        try:
            return self.itogo
        except AttributeError:
            return None

    def __len__(self):
        return len(self.__Positions)

    # __len__ = lambda self: len(self.__Positions)

    def __getitem__(self, index):
        return self.__Positions[index]

    def __iter__(self):
        for position in self.__Positions:
            yield position

    def append_blank(self):
        #TODO: 1. Функция должна принимать параметры, соответвтвующие
        #         параметрам конструктора класса NakPos,
        #         и добавлять в накладную позицию с этмим параметрами.
        self.__Positions.append(mNakPos.NakPosition())

    def append(self, position):
        if not isinstance(position, mNakPos.NakPosition):
            raise ValueError
        self.__Positions.append(position)

    def delete(self, index):
        del self.__Positions[index]

    def __str__(self):
        posit = ""
        num_pos = 1
        for position in self.__Positions:
            posit += "{num}. {position}\n".format(num=num_pos, position=str(position))
            num_pos += 1
        result = \
            "(ID:{id})  (Status:{status})\n" \
            "Накладная\n" \
            "{num_pos}" \
            "Итого {itogo}".format(id=str(self._id), status=str(self._status),
                                   num_pos=posit, itogo=self._itogo)
        return result


if __name__ == '__main__':
    D = create()
    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =', D.id)
    except AttributeError:
        print('<NONE>')
    print(D.itogo)

    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =', D.id)
    except AttributeError:
        print('<NONE>')
