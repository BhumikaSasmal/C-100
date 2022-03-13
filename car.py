class Car(object):
    def __init__(self,color,model,company,speed):
        self.color= color
        self.model = model
        self.company=company
        self.speed= speed
    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("accelerate")
Car = Car("black","abc","xyz",70)
print(Car.color)
print(Car.speed)
Car.stop()