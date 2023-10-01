class Car:
    def __init__(melf, model, color):
        melf.model = model
        melf.color = color

    def display_info(melf):
        print(f'Model: {melf.model}, Color {melf.color} ')

car1 = Car('Toyota Selica' , 'Blue')
car1.display_info()
