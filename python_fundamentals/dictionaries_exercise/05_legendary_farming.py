farming = {}
find_artefact = False
shards, fragments, motes = 0, 0, 0
while True:
    materials = input().split()

    for index in range(0, len(materials), 2):
        quantity = materials[index]
        material = materials[index + 1].lower()
        if material not in farming:
            farming[material] = 0
        farming[material] += int(quantity)

        for material, quantity in farming.items():
            if material == "shards" and quantity >=250:
                print("Shadowmourne obtained!")
                farming[material] -= 250
                find_artefact = True
            elif material == "fragments" and quantity >=250:
                print("Valanyr obtained!")
                farming[material] -= 250
                find_artefact = True
            elif material == "motes" and quantity >=250:
                print("Dragonwrath obtained!")
                farming[material] -= 250
                find_artefact = True
        if find_artefact:
            break
    if find_artefact:
        break

if "shards" in farming:
    shards = farming['shards']
if "fragments" in farming:
    fragments = farming['fragments']
if "motes" in farming:
    motes = farming['motes']

print(f"shards: {shards}")
print(f"fragments: {fragments}")
print(f"motes: {motes}")
for material, quantity in farming.items():
    if material != "shards" and material != "fragments" and material != "motes":
        print(f"{material}: {quantity}")


