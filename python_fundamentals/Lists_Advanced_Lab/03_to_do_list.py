notes = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority,note)

result = [element for element in notes if element !=0]
print(result)

# def todo_notes():
#     result_list = []
#     while True:
#         to_do_notes = input()
#         if to_do_notes == 'End':
#             break
#         result_list.append(to_do_notes)
#
#     sorted_notes = sorted(result_list, key=lambda x: int(x.split('-')[0]))
#     next_notes = [note.split('-')[1] for note in sorted_notes]
#     return next_notes
#
# print(todo_notes())
