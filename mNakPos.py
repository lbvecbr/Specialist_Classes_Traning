class NakPosition(object):
    def __init__(self):
        pass

    id      = property(lambda self: self.__Id    )
    title   = property(lambda self: self.__Title )
    unit    = property(lambda self: self.__Unit  )
    price   = property(lambda self: self.__Price )
    amount  = property(lambda self: self.__Amount)
    summa   = property(lambda self: self.__Summa ) 