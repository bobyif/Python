from pydoc import doc


class Characters:
    def __init__(self, id , name, color, attack_damage, health, shield, capacity):
        self.id = id
        self.name = name
        self.color = color
        self.attack_damage = attack_damage
        self.health = health
        self.shield = shield
        self.capacity = capacity

    def takeDamage(self, decreaseHealth):
        if  self.shield >= decreaseHealth:
            self.shield -= decreaseHealth
        else:
            self.health += self.shield
            self.shield = 0
            self.health -= decreaseHealth


    def checkShield(self):
        print(self.shield)
    def checkHealth(self):
        print(self.health)
    def attack(self, id):
        if id == "1":
            self.attack_damage -= 50
            self.health -= self.attack_damage
        if id == "2":
            if  Millennium_Falcon.shield >= self.attack_damage:
                Millennium_Falcon.shield -= self.attack_damage
            else:
                Millennium_Falcon.health += Millennium_Falcon.shield
                Millennium_Falcon.shield = 0
                Millennium_Falcon.health -= (self.attack_damage + 200)
        if id == "3":
            if  Ebon_Hawk.shield >= self.attack_damage:
                Ebon_Hawk.shield -= self.attack_damage
            else:
                Ebon_Hawk.health += Ebon_Hawk.shield
                Ebon_Hawk.shield = 0
                Ebon_Hawk.health -= self.attack_damage

    def Heal(self, increaseHealth):
        Ebon_Hawk.health += increaseHealth


    
Outrider = Characters(1,"Outrider", "black", 50, 100, 200, 90)
Millennium_Falcon = Characters(2, "Millennium_Falcon", "black", 30, 250, 70, 40)
Ebon_Hawk = Characters(3, "Ebon_Hawk", "black", 20, 120, 80, 60)

startGame = True
while startGame:

    userAns = input("\nWhat ship are you chooseing?\n ")


    if userAns == "1":
        Outrider.health += 100
    
        userAns = input("\nWhat would you like to do?\n ")

        if userAns.lower() == "attack":
            userAns = input("\n Who do you want to attack?\n ")
            Outrider.attack(userAns)
            
        if userAns.lower() == "takedamage":
            userAns = input("\n How much damage do you whant to take?\n ")
            Outrider.takeDamage(int(userAns))
            print("Your Shield", end = " ")
            Outrider.checkShield()
            print("Your health", end = " ")
            Outrider.checkHealth()


        if userAns == "IsDestroyed":
            if Outrider.health <= 0:
                startGame = False
                print("You are dead, Game Over")



    if userAns == "2":
        userAns = input("\nWhat would you like to do?\n ")

        if userAns.lower() == "attack":
            userAns = input("\n Who do you want to attack?\n ")
            Millennium_Falcon.attack(userAns)
            
        if userAns.lower() == "takedamage":
            userAns = input("\n How much damage do you whant to take?\n ")
            Millennium_Falcon.takeDamage(int(userAns))
            print("Your Shield", end = " ")
            Millennium_Falcon.checkShield()
            print("Your health", end = " ")
            Millennium_Falcon.checkHealth()

        if userAns == "IsDestroyed":
            if Millennium_Falcon.health <= 0:
                startGame = False
                print("You are dead, Game Over")



    if userAns == "3":
        userAns = input("\nWhat would you like to do?\n ")


        if userAns.lower() == "attack":
            userAns = input("\n Who do you want to attack?\n ")
            Ebon_Hawk.attack(userAns)
            
        if userAns.lower() == "takedamage":
            userAns = input("\n How much damage do you whant to take?\n ")
            Ebon_Hawk.takeDamage(int(userAns))
            print("Your Shield", end = " ")
            Ebon_Hawk.checkShield()
            print("Your health", end = " ")
            Ebon_Hawk.checkHealth()
            
        
        if userAns.lower() == "heal":
            Ebon_Hawk.Heal(50)
            print("Your health is now ")
            Ebon_Hawk.checkHealth()

        if userAns == "IsDestroyed":
            if Ebon_Hawk.health <= 0:
                startGame = False
                print("You are dead, Game Over")
            
            



            

        