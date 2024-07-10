def merge(data, start, end):
    start = max(0, start)
    end = min(len(data) - 1, end)
    merged_part = ''.join(data[start:end + 1])
    return data[:start] + [merged_part] + data[end + 1:]

def divide(data, index, partitions):
    if partitions == 0:
        return data
    element = data[index]
    part_length = len(element) // partitions
    extra_chars = len(element) % partitions
    new_parts = []
    start = 0
    for i in range(partitions):
        if extra_chars > 0:
            new_parts.append(element[start:start + part_length + 1])
            start += part_length + 1
            extra_chars -= 1
        else:
            new_parts.append(element[start:start + part_length])
            start += part_length
    return data[:index] + new_parts + data[index + 1:]

data = input().split()
while True:
    command = input()
    if command == "3:1":
        break
    command_parts = command.split()
    action = command_parts[0]
    if action == "merge":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])
        data = merge(data, start_index, end_index)
    elif action == "divide":
        index = int(command_parts[1])
        partitions = int(command_parts[2])
        data = divide(data, index, partitions)

print(' '.join(data))