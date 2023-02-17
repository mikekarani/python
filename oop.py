class EmobilisStudent:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def hello_me(self):
       print(f"My name is {self.name} and im {self.age} years old")

class valentines:
    def __init__(self, couplename,reservation,tableno):
      self.couplename=couplename
      self.reservation=reservation
      self.tableno=tableno
    def hotel(self):
     print(f"The following {self.couplename} has a booking for {self.reservation} at table number {self.tableno}")

#assignment
class magari:
    def __init__(self, mode ,make, year):
        self.mode=mode
        self.make=make
        self.year=year
    def cars(self):
        print(f"Our cars are of the following properties:{self.mode},{self.make},{self.year}")


#creating an object
myobj=EmobilisStudent("Karani wamichael",22)
myobj.hello_me()


myobj2=valentines("furahas","YFVDYRCF",7)
myobj2.hotel()




myobj3=magari("modelS","TESLA",2012)
myobj3.cars()
myobj3=magari("M8","BMW",2007)
myobj3.cars()
myobj3=magari("V8","TOYOTA",2016)
myobj3.cars()
myobj3=magari("E350","MERCEDEZ",2020)
myobj3.cars()


def minval(TESLA,BMW,TOYOTA,MERCEDEZ):
    return min(TESLA,BMW,TOYOTA,MERCEDEZ)
result=minval(2012,2007,2016,2020)
print(result)


class ujuaji:
    def __init__(wamboto,artist,song):
        wamboto.artist=artist
        wamboto.song=song
    def why(wamboto):
        print(f"{wamboto.artist} has sang {wamboto.song} which was a major hit intenationally")

myobj4=ujuaji("sauti sol", "suzanna")
myobj4.why()
myobj4=ujuaji("ayrra star", "rush")
myobj4.why()
myobj4=ujuaji("bien", "bald man anthem")
myobj4.why()
myobj4=ujuaji("nameless", "repsect the hustle")
myobj4.why()