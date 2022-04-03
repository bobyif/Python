class Room :
    def __init__(self, RoomNumber , pricePerNight, cleaned_rooms, tourist_name, workerId,name, room, stayDays, isAllInclusive):
        self.RoomNumber = RoomNumber
        self.pricePerNight = pricePerNight
        self.cleaned_rooms = cleaned_rooms
        self.isAllInclusive = isAllInclusive
        
    def abstract(self, room_number):
        self.RoomNumber +=  room_number 
    
    
    def Suite(self):
        self.pricePerNight += 50

    def Apartment(self):
        if self.RoomNumber > 10:
            pricePerNight = 150
        else:
            pricePerNight = 100


    def Cleaner (self, cleaned_rooms):
        cleaned_rooms = [1 ,3, 4, 8, 15 ,25 ,33]
        print(cleaned_rooms)

    def cleaner_greet(self, tourist_name):
            print("Enjoy your stay" + self.tourist_name)
        
    def clean(self,cleaned_rooms,RoomNumber):
            cleaned_rooms = cleaned_rooms.append(RoomNumber)

    def Receptionist(self, taken_rooms):
        taken_rooms = [2, 34, 5, 14 ,22, 25]
        print(taken_rooms)


    def Receptionist_Greet(self, tourist_name):
        print("Welcome to the hotel" + self.tourist_name)


    def Tourist(self,name, age, isAllInclusive):
        print(str(name) + " total price for the stay - 3300.00EUR")

    def relax(self, isAllInclusive):
        if isAllInclusive == "Yes":
            print("Feels good to make fat stacks coding")
        else:
            print(":)")
        

    Tourist("Ivan", 22, True)
    Tourist("Ivan", 22, True)
    Tourist("Ivan", 22, True)


    relax("Nikolay")
    relax("Ivan")
    relax("dimitar")

    Cleaner.clean(3)

    Receptionist_Greet("ivan")
    Receptionist_Greet("nikolay")
    Receptionist_Greet("dimitar")

    cleaner_greet("ivan")
    cleaner_greet("nikolay")


    ("Total cleaned rooms - %d%n", Cleaner())
    ("Total taken rooms - %d%n", Receptionist) 

