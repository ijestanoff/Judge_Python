input_list = input().split()
while True:
    command = input().split()
    if command[0] == "3:1":
        break
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < len(input_list)-1:
            if start_index < 0:
                start_index = 0
            if end_index > 0:
                if end_index >= len(input_list):
                    end_index = len(input_list) - 1
                for index in range(end_index, start_index, -1):
                    input_list[index-1] += input_list[index]
                    input_list.pop(index)
    elif command[0] == "divide":
        divide_index = int(command[1])
        divide_parts = int(command[2])
        if divide_parts > 0 and divide_index >= 0:
            part_len = len(input_list[divide_index])
            original_text = input_list[divide_index]
            symbol_step = part_len // divide_parts
            input_list.pop(divide_index)
            for partition in range(divide_parts-1):
                part_text = original_text[partition * symbol_step: partition * symbol_step + symbol_step:]
                input_list.insert(divide_index + partition, part_text)
                last_part = original_text[partition * symbol_step + symbol_step::]
                last_index = divide_index + partition + 1
            input_list.insert(last_index, last_part)
print(" ".join(input_list))
