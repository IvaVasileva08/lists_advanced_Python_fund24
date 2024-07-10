def add_lesson(schedule, lesson_title):
    if lesson_title not in schedule:
        schedule.append(lesson_title)

def insert_lesson(schedule, lesson_title, index):
    if lesson_title not in schedule:
        schedule.insert(index, lesson_title)

def remove_lesson(schedule, lesson_title):
    if lesson_title in schedule:
        schedule.remove(lesson_title)
        exercise = lesson_title + "-Exercise"
        if exercise in schedule:
            schedule.remove(exercise)


def swap_lessons(schedule, lesson_title1, lesson_title2):
    if lesson_title1 in schedule and lesson_title2 in schedule:
        index1, index2 = schedule.index(lesson_title1), schedule.index(lesson_title2)
        schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
        exercise1, exercise2 = lesson_title1 + "-Exercise", lesson_title2 + "-Exercise"
        if exercise1 in schedule:
            schedule.remove(exercise1)
            schedule.insert(schedule.index(lesson_title1) + 1, exercise1)
        if exercise2 in schedule:
            schedule.remove(exercise2)
            schedule.insert(schedule.index(lesson_title2) + 1, exercise2)

def add_exercise(schedule, lesson_title):
    if lesson_title in schedule:
        exercise = lesson_title + "-Exercise"
        if exercise not in schedule:
            schedule.insert(schedule.index(lesson_title) + 1, exercise)
    else:
        schedule.append(lesson_title)
        schedule.append(lesson_title + "-Exercise")

schedule = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    parts = command.split(":")
    action = parts[0]
    if action == "Add":
        add_lesson(schedule, parts[1])
    elif action == "Insert":
        insert_lesson(schedule, parts[1], int(parts[2]))
    elif action == "Remove":
        remove_lesson(schedule, parts[1])
    elif action == "Swap":
        swap_lessons(schedule, parts[1], parts[2])
    elif action == "Exercise":
        add_exercise(schedule, parts[1])

for index, lesson in enumerate(schedule, 1):
    print(f"{index}.{lesson}")