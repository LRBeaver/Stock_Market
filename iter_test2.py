class A(object):
    def __init__(self):
        self.myinstatt1 = 'one'
        self.myinstatt2 = 'two'
    def mymethod(self):
        pass

a = A()
for attr, value in a.__dict__.items():
    print(attr, value)