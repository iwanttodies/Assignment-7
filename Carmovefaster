class car:
    def __init__(self,resignation , max_speed):
           
        self.resignation=resignation
        self.maxspeed=max_speed
        self.currentspeed=0
        self.distancetravelled=0
    def accelerate(self,speed):
         self.currentspeed+=speed
         if self.currentspeed>self.maxspeed:
             self.currentspeed=self.maxspeed
         if self.currentspeed<0:
             self.currentspeed=0

#reg_num=input("Enter your resignation number pls : ")
#speedmaxxing=int(input("Enter your car maxium speed : "))  
#Car=car(reg_num,speedmaxxing)
#Just in case 

Car=car("ABC123",142)
Car.accelerate(+30)
Car.accelerate(+70)
Car.accelerate(+50)
print("Car current speed prior to full stop:",Car.currentspeed)

Car.accelerate(-200)

print("---Car stats---")
print("Resignation number: ",Car.resignation)
print("Cars speed limit: ",Car.maxspeed,"km/h")
print("Cars current speed: ",Car.currentspeed,"km/h")
print("Cars travelled distance: ",Car.distancetravelled,"Km")

       