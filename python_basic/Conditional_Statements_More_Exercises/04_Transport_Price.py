TAXI_INIT_PRICE = 0.70
TAXI_DAY_PRICE = 0.79
TAXI_NIGHT_PRICE = 0.90
BUS_PRICE = 0.09
BUS_MIN_DISTANCE = 20
TRAIN_PRICE = 0.06
TRAIN_MIN_DISTANCE = 100
distance = int(input())
day_state = input()
if distance >= TRAIN_MIN_DISTANCE:
    print(f"{distance * TRAIN_PRICE:.02f}")
elif distance >= BUS_MIN_DISTANCE:
    print(f"{distance * BUS_PRICE:.02f}")
else:
    taxi_charge=0
    if day_state == "day":
        taxi_charge = TAXI_INIT_PRICE + distance * TAXI_DAY_PRICE
    if day_state == "night":
        taxi_charge = TAXI_INIT_PRICE + distance * TAXI_NIGHT_PRICE
    print(f"{taxi_charge:.02f}")

