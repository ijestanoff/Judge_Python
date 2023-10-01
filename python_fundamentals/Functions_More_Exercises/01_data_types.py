def data_type(type_of_data, data):
    if type_of_data == "int":
        print(int(data) * 2)
    elif type_of_data == "real":
        print(f"{float(data) * 1.5:.2f}")
    else:
        print(f"${data}$")


type_of_data = input()
data = input()
data_type(type_of_data, data)
