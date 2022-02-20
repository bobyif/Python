
beers = 200
orders_beer = 0
deliveries_beer = 0

wines = 300
orders_wine = 0
deliveries_wine = 0


while True:
    user_input= input("")
    if user_input == "END":
        break
    
    Type, count = str(user_input).split(":")

    amount = int(count)



    if amount > 0:
        if user_input[:5] == "Beers":
            beers = beers + amount
            deliveries_beer+= 1

    if amount < 0:
        if user_input[:5] == "Beers":
            beers = beers + amount
            orders_beer+= 1

    if amount > 0:
        if user_input[:5] == "Wines":
            wines = wines + amount
            deliveries_wine+= 1

    if amount < 0:
        if user_input[:5] == "Wines":
            wines = wines + amount
            orders_wine+= 1



print("Wines :" + str(wines))
print("Deliveries :" + str(deliveries_wine))
print("Orders :" + str(orders_wine))
print("Beers :" + str(beers))
print("Deliveries :" + str(deliveries_beer))
print("Orders :" + str(orders_beer))

