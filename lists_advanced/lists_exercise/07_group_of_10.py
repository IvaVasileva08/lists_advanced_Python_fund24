num = input().split(", ")
text = [int(n) for n in num]
group10 =[]
group20 =[]
group30 =[]
group40 =[]
group50 =[]
for numbers in text:
    if numbers <= 10:
        group10.append(numbers)
    elif 10 < numbers <= 20:
        group20.append(numbers)
    elif 20 < numbers <= 30:
        group30.append(numbers)
    elif 30 < numbers <= 40:
        group40.append(numbers)
    elif 40 < numbers <= 50:
        group50.append(numbers)

print(f"Group of 10's: {group10}")
print(f"Group of 20's: {group20}")
print(f"Group of 30's: {group30}")
print(f"Group of 40's: {group40}")
print(f"Group of 50's: {group50}")