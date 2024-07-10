mystring = input().split(" ")
happines_factor = int(input())
mystring = list(map(lambda x: int(x) * happines_factor, mystring))
new_filter = list(filter(lambda x: x >= (sum(mystring) / len(mystring)), mystring))
if len(new_filter) >= len(mystring) / 2:
    print(f"Score: {len(new_filter)}/{len(mystring)}. Employees are happy!")
else:
    print(f"Score: {len(new_filter)}/{len(mystring)}. Employees are not happy!")