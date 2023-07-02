VIDEO_CARD_PRICE = 250.00
peter_budget = float(input())
video_card_quantity = int(input())
PROCESSOR_PRICE = VIDEO_CARD_PRICE * video_card_quantity * 0.35
RAM_PRICE = VIDEO_CARD_PRICE * video_card_quantity * 0.10
processor_quantity = int(input())
ram_quantity = int(input())
budget = VIDEO_CARD_PRICE * video_card_quantity + PROCESSOR_PRICE * processor_quantity + RAM_PRICE * ram_quantity
if video_card_quantity > processor_quantity:
    budget *= 0.85
if budget <= peter_budget:
    print(f"You have {peter_budget - budget:.02f} leva left!")
else:
    print(f"Not enough money! You need {budget - peter_budget:.02f} leva more!")