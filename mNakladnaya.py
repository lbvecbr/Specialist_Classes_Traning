import mDocument
import mNakPos

def create():
    return Nakladnaya(status = mDocument.Document.New )

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

    def get_position(self, index):
        return self.__Positions[index]

    def append_blank(self):
        self.__Positions.append(mNakPos.NakPosition)

    def append(self, position):
        if not isinstance(position, mNakPos.NakPosition):
            raise ValueError
        self.__Positions.append(position)

    def delete(self, index):
        del self.__Positions[index]

    def dump (self):
        Posit = ""
        K = 1
        for P in self.__Positions:
            Posit += "%d.\n" % (K,)
            K += 1
        Result = "(ID:%s)  (Status:%s)\n" % (str(self._id), str(self._status))
        Result += "Накладная\n"
        Result += "%s" % (Posit,)
        Result += "Итого %s" % (self._itogo,)
        return Result



if __name__ == '__main__':
    D = create()
    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =',  D.id)
    except AttributeError:
        print('<NONE>')
    print(D.itogo)

    try:
        print('Status = ', D.status)
    except AttributeError:
        print('<NONE>')
    try:
        print('ID     =',  D.id)
    except AttributeError:
        print('<NONE>')
