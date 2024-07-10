def update_version(version):
    parts = version.split(".")

    i = int(parts[0])
    j = int(parts[1])
    k = int(parts[2])
    k+=1
    if k > 9:
        k = 0
        j += 1
        if j > 9:
            j = 0
            i += 1
    return i, j, k

current_version = input()
i,j,k = update_version(current_version)
print(f"{i}.{j}.{k}")