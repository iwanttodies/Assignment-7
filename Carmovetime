class car:
    def __init__(self,resignation , max_speed):
           
        self.resignation=resignation
        self.maxspeed=max_speed
        self.currentspeed=0
        self.distancetravelled=2000
    def accelerate(self,speed):
         self.currentspeed+=speed
         if self.currentspeed>self.maxspeed:
             self.currentspeed=self.maxspeed
         if self.currentspeed<0:
             self.currentspeed=0
    def drive(self,hours):
        self.time=hours
        self.distancetravelled+=hours*self.currentspeed    
#reg_num=input("Enter your resignation number pls : ")
#speedmaxxing=int(input("Enter your car maxium speed : "))  
#Car=car(reg_num,speedmaxxing)
#Just in case 

Car=car("ABC123",142)
Car.accelerate(+60)

print("Car current speed: ",Car.currentspeed)
Car.drive(1.5)


print("---Car stats---")
print("Resignation number: ",Car.resignation)
print("Cars speed limit: ",Car.maxspeed,"km/h")
print("Cars current speed: ",Car.currentspeed,"km/h")
print("car travelled time: ",Car.time,"hrs")
print("Cars travelled distance: ",Car.distancetravelled,"Km")
