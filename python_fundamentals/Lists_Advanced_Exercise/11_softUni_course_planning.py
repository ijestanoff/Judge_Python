initial_schedule = input().split(", ")
while True:
    command = input().split(":")
    if command[0] == "course start":
        break
    if command[0] == "Add":
        lesson_title = command[1]
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
    if command[0] == "Insert":
        lesson_title = command[1]
        lesson_index = int(command[2])
        if lesson_title not in initial_schedule:
            initial_schedule.insert(lesson_index, lesson_title)
    if command[0] == "Remove":
        lesson_title = command[1]
        lesson_index = initial_schedule.index(lesson_title)
        if lesson_title in initial_schedule:
            if lesson_index + 1 in range(len(initial_schedule)):
                if "Exercise" in initial_schedule[lesson_index + 1]:
                    initial_schedule.pop(lesson_index + 1)
            initial_schedule.remove(lesson_title)
    if command[0] == "Swap":
        first_lesson = command[1]
        second_lesson = command[2]
        if first_lesson in initial_schedule and second_lesson in initial_schedule:
            first_lesson_index = initial_schedule.index(first_lesson)
            second_lesson_index = initial_schedule.index(second_lesson)
            first_lesson_exercise = False
            if first_lesson_index + 1 in range(len(initial_schedule)):
                if "Exercise" in initial_schedule[first_lesson_index + 1]:
                    first_lesson_exercise = True
            second_lesson_exercise = False
            if second_lesson_index + 1 in range(len(initial_schedule)):
                if "Exercise" in initial_schedule[second_lesson_index + 1]:
                    second_lesson_exercise = True
            initial_schedule[first_lesson_index], initial_schedule[second_lesson_index] = \
                initial_schedule[second_lesson_index], initial_schedule[first_lesson_index]
            if first_lesson_exercise and not second_lesson_exercise:
                initial_schedule.insert(second_lesson_index + 1, initial_schedule.pop(first_lesson_index + 1))
            elif not first_lesson_exercise and second_lesson_exercise:
                initial_schedule.insert(first_lesson_index + 1, initial_schedule.pop(second_lesson_index + 1))
            elif first_lesson_exercise and second_lesson_exercise:
                initial_schedule[first_lesson_index + 1], initial_schedule[second_lesson_index + 1] = \
                    initial_schedule[second_lesson_index + 1], initial_schedule[first_lesson_index + 1]
    if command[0] == "Exercise":
        lesson_title = command[1]
        if lesson_title in initial_schedule and f"{lesson_title}-Exercise" not in initial_schedule:
            title_index = initial_schedule.index(lesson_title)
            initial_schedule.insert(title_index + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
            initial_schedule.append(f"{lesson_title}-Exercise")
        # if lesson_title not in initial_schedule:
        #     initial_schedule.append(lesson_title)
        #     lesson_title = lesson_title + "-Exercise"
        #     initial_schedule.append(lesson_title)
        # else:
        #     index_exercise = initial_schedule.index(lesson_title)
        #     if index_exercise + 1 in range(len(initial_schedule)):
        #         if "Exercise" not in initial_schedule[index_exercise + 1]:
        #             lesson_title = lesson_title + "-Exercise"
        #             initial_schedule.insert(index_exercise + 1, lesson_title)
for index_schedule in range(len(initial_schedule)):
    print(f"{index_schedule + 1}.{initial_schedule[index_schedule]}")
