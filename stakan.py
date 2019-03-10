class Stakan(object):

    Position =['skaf', 'stol']

    def __init__(self):
        self.__water = 0.0
        self.__milk = 0.0
        self.__position = 'skaf'

    def add_watter(self, vol):
        if vol < 0:
            raise ValueError
        self.__water += vol

    def add_milk(self, vol):
        if vol < 0:
            raise ValueError
        self.__milk += vol

    def take(self, vol):
        if vol < 0:
            raise ValueError
        if vol > self.total():
            raise Exception
        P = self.part_milk()
        M = self.part_milk() * vol
        W = vol - M
        self.__milk -= M
        self.__water -= W
        return (vol, P)

    def set_position(self, position):
        pass

    def total(self):
        return self.__water + self.__milk

    def part_milk(self):
        return self.__milk / self.total()
    

if __name__ == "__main__":
    St = Stakan() 
    St.add_watter(5.0)
    St.add_milk  (1.0)
    St.add_watter(3.0)
    print(St.total())
    print(St.part_milk())