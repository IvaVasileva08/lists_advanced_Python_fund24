n = int(input())
total_free_chairs = 0
game_on = True
for room in range(1, n+1):
    data = input().split()
    chairs = len(data[0])
    visitors = int(data[1])
    if chairs >= visitors:
        total_free_chairs += chairs - visitors
    else:
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
        game_on = False
if game_on:
    print(f"Game On, {total_free_chairs} free chairs left")