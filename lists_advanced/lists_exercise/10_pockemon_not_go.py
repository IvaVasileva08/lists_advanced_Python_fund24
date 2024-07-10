def capture_pokemon(distances, index):
    if index < 0:
        removed_element = distances.pop(0)
        distances.insert(0, distances[-1])
    elif index >= len(distances):
        removed_element = distances.pop(-1)
        distances.append(distances[0])
    else:
        removed_element = distances.pop(index)

    for i in range(len(distances)):
        if distances[i] <= removed_element:
            distances[i] += removed_element
        else:
            distances[i] -= removed_element

    return removed_element

def main():
    distances = list(map(int, input().split()))
    total_removed_sum = 0

    while len(distances) > 0:
        index = int(input())
        total_removed_sum += capture_pokemon(distances, index)

    print(total_removed_sum)

if __name__ == "__main__":
    main()