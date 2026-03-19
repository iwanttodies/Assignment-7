import random
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
    def drive(self,hours):
        self.distancetravelled+=hours*self.currentspeed    

carlist=[]
for i in range(1,11):
    resignum=(f"ABC-{i}")
    speedmax=random.randint(150,200)    
    ccar=car(resignum,speedmax)
    carlist.append(ccar)
for ccar in carlist:
    print(f'Car:{ccar.resignation}|maxspeed:{ccar.maxspeed}')
while True:
     for ccar in carlist:
        ccar.accelerate(random.randint(-15,15))
        ccar.drive(1)     
     if any(ccar.distancetravelled>=10000 for ccar in carlist):
        break
     
print(f"{'Car':<8} {'Max Speed':>6} {'Curr Speed':>6} {'Distance':>8}")
print("-" * 35)
for ccar in carlist:
    print(f"{ccar.resignation:<8} {ccar.maxspeed:>6} {ccar.currentspeed:>6} {ccar.distancetravelled:>8.1f}")
    


