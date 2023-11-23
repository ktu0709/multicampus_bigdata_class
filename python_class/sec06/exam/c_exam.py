'''
C = make_dataclass('C',
                   [('x', int),
                     'y',
                    ('z', int, field(default=5))],
                   namespace={'add_one': lambda self: self.x + 1}, )
'''

class C:
    def __init__(self,x:int,y,z:int = 5):
        self.x=x
        self.y=y
        self.z=z

    def add_one(self):
        return self.x+1
