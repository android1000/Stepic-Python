class MoneyBox:

    def __init__(self, capacity,current=0):
        self.capacity=capacity
        self.current=current

    def can_add(self, v):
        if self.current+v<=self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.current+=v
