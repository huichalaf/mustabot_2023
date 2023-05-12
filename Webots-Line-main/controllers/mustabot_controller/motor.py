class MOTOR:
    def __init__(self, robot, name):
        self.motor = robot.getDevice(name)
        self.motor.setPosition(float('inf'))
        self.motor.setVelocity(0)
        self.name = name

    def setVelocity(self, velocity):
        self.motor.setVelocity(-velocity)
    
    def getVelocity(self):
        return self.motor.getVelocity()

    def getName(self):
        return self.name
    
    def stop(self):
        self.motor.setVelocity(0)

class ENCODER:
    def __init__(self, robot, name):
        self.encoder = robot.getDevice(name)
        self.encoder.enable(32)
        self.name = name
        self.position = 0
        self.start_position = 0
    
    def getValue(self):
        self.position = self.encoder.getValue() - self.start_position
        return self.position
    
    def getName(self):
        return self.name

    def set_start_position(self):
        self.start_position = self.encoder.getValue()