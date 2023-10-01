countries = input().split(", ")
capitals = input().split(", ")
countries_capitals = {country: capital for country, capital in zip(countries, capitals)}
for key, val in countries_capitals.items():
    print(f"{key} -> {val}")
