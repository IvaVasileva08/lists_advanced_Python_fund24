"""string1 = input().split()
for word in string1:
    if len(word) % 2 == 0:
        print (word)"""

string1 = input()
string2 = [word for word in string1.split() if len(word) % 2 == 0]
for word in string2:
    print(word)