###10_9
##class Bear:
##    def eats(self):
##        return 'berries'
##class Rabbit:
##    def eats(self):
##        return 'clover'
##class Octothorpe:
##    def eats(self):
##        return 'campers'
##
##b = Bear()
##r = Rabbit()
##o = Octothorpe()
##
##print(b.eats())
##print(r.eats())
##print(o.eats())


10_10
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone= SmartPhone()
    def does(self):
        return f'''I have many attachments:
my laser, to {self.laser.does()}.
my claw:{self.claw.does()}.
my smartphone:{self.smartphone.does()}. '''


robbie = Robot()
print( robbie.does())















    
