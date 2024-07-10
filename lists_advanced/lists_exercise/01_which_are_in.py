string1 = input().split(", ")
string2 = input().split(", ")
result = []
for s1 in string1:
    for s2 in string2:
        if s1 in s2:
            result.append(s1)
            break
print(result)