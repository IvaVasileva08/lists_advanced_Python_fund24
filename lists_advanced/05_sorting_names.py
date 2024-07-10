name_list = input().split(", ")
sort_list = sorted(name_list, key = lambda x: (-len(x), x))
print(sort_list)