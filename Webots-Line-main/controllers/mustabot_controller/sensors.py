from functions import is_green

class IR:
    def __init__(self, robot, name):
        self.ir = robot.getDevice(name)
        self.ir.enable(32)
        self.name = name
    
    def getValue(self):
        return self.ir.getValue()
    
    def getName(self):
        return self.name

class LASER:
    def __init__(self, robot, name):
        self.laser = robot.getDevice(name)
        self.laser.enable(32)
        self.name = name
    
    def getValue(self):
        return self.laser.getValue()
    
    def getName(self):
        return self.name

class COLOR:
    def __init__(self, robot, name):
        self.color = robot.getDevice(name)
        self.color.enable(32)
        self.name = name
        self.color_name = "undefined"
    
    def getValue(self):
        return self.color.getValue()
    
    def getName(self):
        return self.name
    
    def get_color(self):
        print("color: ", self.color.getValue())
        if is_green(self.color.getValue()):
            self.color_name = "green"
        else:
            self.color_name = "undefined"
        return self.color_name
